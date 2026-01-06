const API_URL = process.env.NEXT_PUBLIC_API_URL || 'https://hackathon2-phase2-3tna-3w3v144th-tehreem-asghars-projects.vercel.app/';

type FetchOptions = RequestInit & {
  headers?: Record<string, string>;
};

export const api = {
  async fetch(endpoint: string, options: FetchOptions = {}) {
    const token = localStorage.getItem('token');
    
    const headers: Record<string, string> = {
      'Content-Type': 'application/json',
      ...(options.headers as Record<string, string> || {}),
    };

    if (token) {
      headers['Authorization'] = `Bearer ${token}`;
    }

    const response = await fetch(`${API_URL}${endpoint}`, {
      ...options,
      headers,
    });

    if (response.status === 401) {
       // Optional: Dispatch logout event or handle globally
       // For now, we just return the response and let the caller/context handle it
    }

    return response;
  }
};
