
# Internal Ticketing & Chat Assignment Platform

It is a lightweight internal tool for operations teams to manage tasks, collaborate via threaded group chat, and get instant summaries of discussions with AI support.

## Features
- Task Management with inline status/assignment
- Threaded Chat with real-time WebSocket support
- AI Summarization with entity extraction
- @QAreview auto-triggers QA rules
- Designed for scale: 10k+ tasks

## Getting Started
- Clone, install backend and frontend dependencies
- Set up PostgreSQL or use docker-compose
- Start backend: `uvicorn app.main:sio_app --reload`
- Start frontend: `npm start`

## Tech Stack
FastAPI, React, PostgreSQL, LangChain, socket.io
