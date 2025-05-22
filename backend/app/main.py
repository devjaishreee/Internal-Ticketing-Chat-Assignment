
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import tasks, chat, summarize
from app.db import create_db_and_tables
import socketio

sio = socketio.AsyncServer(cors_allowed_origins="*")
app = FastAPI()
sio_app = socketio.ASGIApp(sio, other_asgi_app=app)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(tasks.router, prefix="/tasks", tags=["Tasks"])
app.include_router(chat.router, prefix="/chat", tags=["Chat"])
app.include_router(summarize.router, prefix="/summarize", tags=["Summarize"])

@app.on_event("startup")
def on_startup():
    create_db_and_tables()

@app.get("/")
def root():
    return {"message": "WebSocket-powered backend"}
