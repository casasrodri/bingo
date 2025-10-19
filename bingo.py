from pathlib import Path

from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI()

# Ruta al archivo HTML
html_path = Path(__file__).parent / "index.html"


# Servir el HTML principal
@app.get("/", response_class=HTMLResponse)
def serve_bingo():
    return html_path.read_text(encoding="utf-8")


# Si tenés recursos estáticos (JS, CSS, imágenes)
app.mount("/static", StaticFiles(directory="static"), name="static")

# uvicorn bingo:app --reload --port 8000
