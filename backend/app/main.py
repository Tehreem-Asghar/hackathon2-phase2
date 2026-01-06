from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import ValidationError

from app.api.routes import auth, todos
from app.core.config import settings
from app.db.session import engine
from app.models.user import User
from app.models.todo import Todo

from sqlalchemy import text

app = FastAPI(title=settings.PROJECT_NAME)

# Set all CORS enabled origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://127.0.0.1:3000" , "http://127.0.0.1:8000/"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth, prefix="/api/auth", tags=["auth"])
app.include_router(todos, prefix="/api/todos", tags=["todos"])

@app.on_event("startup")
async def on_startup():
    async with engine.begin() as conn:
        # Create tables if they don't exist
        await conn.run_sync(User.metadata.create_all)
        await conn.run_sync(Todo.metadata.create_all)
        
        # Manually add 'name' column if it's missing (since create_all doesn't handle migrations)
        try:
            await conn.execute(text('ALTER TABLE "user" ADD COLUMN IF NOT EXISTS name VARCHAR'))
            await conn.commit()
        except Exception as e:
            print(f"Migration note: {e}")

@app.get("/")
async def root():
    return {"message": "Hello World"}