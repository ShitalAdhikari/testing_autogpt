import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from nicegui import ui, app as nicegui_app

from backend import app as backend_app
from frontend import create_ui

# Combine FastAPI and NiceGUI
app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

# Mount the backend app
app.mount("/api", backend_app)

# Create the frontend UI
create_ui()

# Mount the NiceGUI app
app.mount("/", nicegui_app)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)