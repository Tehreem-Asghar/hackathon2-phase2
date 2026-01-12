<!--
Sync Impact Report:
Version change: 1.0.0 → 2.0.0
Modified principles: (none)
Added sections:
  - Phase III Technology Matrix (Detailed)
Removed sections: (none)
Templates requiring updates:
  - plan-template.md: ✅ No changes needed
  - spec-template.md: ✅ No changes needed
  - tasks-template.md: ✅ No changes needed
Follow-up TODOs: (none)
-->

# Full-Stack Todo App Constitution

## Core Principles

### I. Phase-Governed Development
The project follows a strict phased development model where technology choices are bounded by the current phase. Phase I focuses on backend API only. Phase II introduces web frontend, authentication, and database. Phase III introduces AI agents and ChatKit. Technologies from later phases MUST NOT be introduced prematurely.

### II. Technology Isolation
Each phase has a defined, immutable technology matrix. Once a phase technology stack is established, deviations require explicit ADR approval. The technology matrix is the single source of truth for what technologies are permitted at each phase.

### III. Incremental Validity
Every phase deliverable must be independently functional and deliver value. Phase I produces a working REST API. Phase II produces a complete full-stack application. Phase III adds AI capabilities. No phase dependencies that require incomplete work from later phases.

### IV. API-First Design (Phase I Priority)
Backend API must be designed and implemented before any frontend work begins in Phase II. The API should be fully documented and independently testable via tools like curl, Postman, or other HTTP clients.

### V. Test Discipline
Automated tests must be written before implementation (TDD for business logic) or immediately after implementation (integration tests). Each user story must be independently testable without requiring implementation of other stories.

### VI. Minimal Complexity
YAGNI principle enforced. No abstractions, patterns, or infrastructure should be added for hypothetical future needs. Start simple, add complexity only when a concrete need emerges and cannot be solved simply.

### VII. Observability
All system components must emit structured logs. API endpoints must log request/response summaries with trace IDs. Errors must be captured with context and stack traces.

## Technology Matrix

### Phase I: Backend API Only
- **Backend**: Python REST API (FastAPI recommended)
- **Database**: SQLite for local development (migrations required)
- **ORM/Data Layer**: SQLModel or equivalent
- **Testing**: pytest with pytest-asyncio
- **Documentation**: OpenAPI/Swagger (auto-generated from FastAPI)
- **Architecture**: REST API with modular service layer
- **Authentication:** Better Auth (handling User Signup/Signin)
- **Security:** JWT Token verification (Frontend sends Token, Backend verifies via Shared Secret `BETTER_AUTH_SECRET`)

**Allowed**: REST API development, database schema design, business logic, API testing
**Forbidden**: Web frontend, authentication systems, cloud databases, AI/agent frameworks

### Phase II: Full-Stack Web Application
- **Backend**: Python REST API (continues from Phase I)
- **Database**: Neon Serverless PostgreSQL (migrate from SQLite)
- **ORM/Data Layer**: SQLModel or equivalent (continues from Phase I)
- **Frontend**: Next.js (React, TypeScript)
- **Authentication:** Better Auth (handling User Signup/Signin)
- **Security:** JWT Token verification (Frontend sends Token, Backend verifies via Shared Secret `BETTER_AUTH_SECRET`)
- **Testing**: pytest (backend), Jest/React Testing Library (frontend)
- **Architecture**: Full-stack web application with API + UI

**Allowed**: Web frontend development, authentication, Neon PostgreSQL, full-stack integration
**Forbidden**: AI/agent frameworks, advanced cloud infrastructure, orchestration systems

### Phase III: Todo AI Chatbot
- **Backend**: Python FastAPI (continues from Phase II)
- **Database**: Neon Serverless PostgreSQL (continues from Phase II)
- **Frontend**: Next.js + OpenAI ChatKit
- **AI Framework**: OpenAI Agents SDK
- **MCP Server**: Official MCP SDK
- **Architecture**: Stateless, database-backed conversation history
- **Tools**: MCP Tools (`add_task`, `list_tasks`, `complete_task`, `delete_task`, `update_task`)

**Allowed**: AI agent implementation, MCP server integration, ChatKit UI, natural language task management
**Forbidden**: Complex microservices, orchestration systems (unless required by Agents SDK)

## Project Standards

### Code Quality
- Python code must pass mypy type checking
- TypeScript code must use strict mode and pass tsc
- All code must pass configured linters (ruff for Python, ESLint for TypeScript)
- Maximum function complexity: Cyclomatic complexity < 10
- Maximum file length: < 500 lines (enforced with exceptions requiring justification)

### Testing Standards
- Unit tests: Isolated, mock external dependencies, test business logic
- Integration tests: Test API contracts and database interactions
- Contract tests: Verify API contracts match OpenAPI spec
- Test coverage: Minimum 80% for business logic (no minimum for infrastructure code)

### Security Standards
- All user inputs must be validated at API boundaries
- Secrets must be stored in environment variables or .env files (never committed)
- Authentication required for all write operations in Phase II
- Database queries must use parameterized statements (no raw SQL concatenation)
- Passwords must be hashed using bcrypt or Argon2

### Performance Standards
- API endpoints: < 200ms p95 latency for simple operations
- Database queries: < 50ms p95 for indexed lookups
- Frontend: < 3s initial page load (Lighthouse score > 90)
- Memory: API service < 512MB, frontend bundle < 2MB

## Governance

### Amendment Procedure
1. Proposal: Document proposed change with rationale and impact analysis
2. Review: All core principles must be re-evaluated for conflicts
3. ADR Creation: For technology stack changes or governance process changes
4. Versioning: Update CONSTITUTION_VERSION following semantic versioning rules
5. Consistency Check: Update dependent templates (plan, spec, tasks) as needed
6. Ratification: Commit with clear message describing amendment scope

### Versioning Policy
- **MAJOR**: Backward-incompatible changes (e.g., removing a principle, changing phase technology stack)
- **MINOR**: New principle or section added, material expansion of guidance
- **PATCH**: Clarifications, wording improvements, typo fixes, non-semantic refinements

### Compliance Review
- All feature specs must reference the constitution for phase context
- All implementation plans must include a Constitution Check section
- Technology decisions outside the current phase's matrix require explicit ADR
- Violations of non-negotiable principles (e.g., "NON-NEGOTIABLE") must be escalated to governance review

### Complexity Justification
If a feature requires violating YAGNI or minimal complexity principles:
1. Document the specific violation
2. Explain why simpler alternatives are insufficient
3. Describe the problem this complexity solves
4. Create an ADR capturing the tradeoff analysis
5. Review must approve before implementation

**Version**: 2.0.0 | **Ratified**: 2026-01-08 | **Last Amended**: 2026-01-08