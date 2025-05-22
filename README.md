
# Internal Ticketing & AI-Enhanced Collaboration System

This project is a full-stack internal ticketing and threaded chat system designed to streamline task management and operational collaboration within an organization. It features real-time updates, threaded group communication, inline status management, and built-in AI-powered summarization and quality control.

---

## Overview

This platform enables operations teams to:
- **View and manage tasks** in a scalable, real-time list
- **Engage in threaded discussions** on a per-task basis with live updates
- **Generate AI-powered summaries** of discussions for quick onboarding
- **Run quality checks** on final replies using configurable rule engines

The entire stack is built for scale, clean code readability, extensibility, and production-readiness. This project was crafted from scratch to showcase my capabilities in designing scalable, AI-integrated, user-centric systems with clean UI and reliable backend architecture.

---

##  What I Built

| Layer       | Feature |
|-------------|---------|
| **Frontend** | Built using React + TypeScript with components for task list, chat pane, summarizer, and QA feedback. Virtualized list support for 10,000+ tasks. |
| **Backend** | FastAPI-based REST + WebSocket backend that serves tasks, messages, and AI summaries. Integrated with PostgreSQL using SQLAlchemy. |
| **AI Engine** | LangChain + OpenAI (or Ollama) pipeline to summarize discussions and extract actionable items (links, phone numbers). |
| **QA Engine** | Rule-based YAML-driven engine triggered via `@QAreview` that checks formatting, content completeness, and best practices. |
| **Realtime** | socket.io-based push system to broadcast task or message updates to all users instantly. |
| **DevOps** | Dockerized full stack with `docker-compose` setup for seamless local or cloud deployment. |

---

## Key Features

### Task Management
- Inline dropdowns for status updates (`Logged → Ongoing → Reviewed → Done`)
- Tagging and color-coded highlights for overdue or high-priority tickets
- Assignment control to reallocate operators in real time

### Threaded Group Chat
- Message threading via `parent_id`
- Chronologically sorted, collapsible chat window per task
- Real-time messaging using socket.io

### Summarization Engine
- One-click summary of the discussion using LangChain with map-reduce strategy
- Automatically extracts relevant links, contact numbers, and action points
- Summary displayed at top of chat pane for context

### Quality Assurance
- Typing `@QAreview` in any message triggers QA bot response
- Configurable checks:
  - Link presence
  - Phone number formatting
  - Message length / empty content
- Rules defined in `qa_rules.yaml` for easy extension

---

##  Tech Stack

| Layer      | Technology            |
|------------|------------------------|
| Frontend   | React, TypeScript, socket.io-client |
| Backend    | FastAPI, SQLAlchemy, socket.io-server |
| Realtime   | WebSockets via socket.io |
| AI         | LangChain, OpenAI / Ollama |
| Database   | PostgreSQL             |
| Deployment | Docker, Docker Compose |

---

## Getting Started

### Prerequisites
- Node.js ≥ 18
- Python ≥ 3.9
- PostgreSQL running locally (or via Docker)
- OpenAI API Key or local LLM setup (Ollama)

### Backend Setup

```bash
cd backend
python -m venv venv && source venv/bin/activate
pip install -r requirements.txt
cp .env.example .env  # Configure DB and OPENAI_API_KEY
python scripts/seed_data.py  # Optional dummy data
uvicorn app.main:sio_app --reload
```

### Frontend Setup

```bash
cd frontend
npm install
npm start
```

---

## Docker Deployment

Spin everything up at once:

```bash
docker-compose up --build
```

- Frontend → http://localhost:3000  
- Backend → http://localhost:8000  
- PostgreSQL DB → port 5432

---

## Architecture Diagram

```
React UI ↔ WebSocket ↔ FastAPI Backend ↔ PostgreSQL
                       ↕
                     LangChain (Summarizer)
                       ↕
                 YAML Rule Engine (@QAreview)
```

---

## Project Structure

```
.
├── backend/
│   ├── app/
│   ├── models/        # SQLAlchemy models
│   ├── routers/       # Task, chat, summarize APIs
│   ├── services/      # Summarizer, QA engine
│   ├── schemas/       # Pydantic types
│   └── main.py        # FastAPI + socket.io app
├── frontend/
│   └── src/components/ # TaskList, ChatPane, SummarizeButton
├── ai/                # summarizer.py, qa_rules.yaml, qa_engine.py
├── docker-compose.yml
└── README.md
```

---

##  Demo & Screenshots

- Record a 2-min Loom walkthrough of:
  - Task creation
  - Chatting with replies
  - Using the summarize button
  - Triggering `@QAreview`
- Optionally embed screenshots in `/docs/screenshots/`

---

##  Why This Stands Out

- Designed for scale: React virtualization + indexed SQL
- AI integration is modular and optional (OpenAI or local)
- QA engine makes it production-ready for client teams
- Fully dockerized, documented, and deployable in minutes

---


