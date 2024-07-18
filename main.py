import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from nicegui import ui, app as nicegui_app

from backend import app as backend_app
from frontend import create_ui

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8080"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/api", backend_app)
create_ui()
app.mount("/", nicegui_app)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)