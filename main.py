import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from nicegui import ui, app as nicegui_app
import warnings

from backend import app as backend_app
from frontend import create_ui
from utils import find_spec_wrapper

def handle_deprecation_warning(message, category, filename, lineno, file=None, line=None):
    if issubclass(category, DeprecationWarning) and "pkgutil.find_loader" in str(message):
        # Ignore this specific deprecation warning
        return
    # For other warnings, use the default behavior
    return warnings.defaultaction(message, category, filename, lineno, file, line)

warnings.showwarning = handle_deprecation_warning

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