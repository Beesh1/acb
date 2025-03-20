# ACB (AI Code Buddy)

A full-stack, AI-powered coding assistant that helps developers pair-program in real time. Think GitHub Copilot, but open-source and built for collaboration. Backend runs on FastAPI with WebSockets, frontend (coming soon) will rock React. This is a learning project to flex full-stack skills and dominate GitHub.

## Status
- **Backend**: FastAPI server with WebSocket, powered by Hugging Face AI for code suggestions — *live and responding with real code!*
- **Frontend**: Not started yet — React incoming.
- **AI**: Using Hugging Face’s `bigcode/starcoder` model via API.

## Tech Stack
- **Backend**: Python 3.12, FastAPI, WebSockets
- **Frontend**: (Planned) React, JavaScript
- **AI**: Hugging Face Inference API
- **Extras**: SQLite (planned), Tailwind CSS (planned)
- **Tools**: `uv` by Astral for project management

## Setup
1. **Clone the repo**:
   ```bash
   git clone https://github.com/Beesh1/acb.git
   cd acb