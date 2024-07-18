from pathlib import Path

from fastapi import APIRouter, WebSocket
from fastapi.requests import Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

router = APIRouter()

PATH_TEMPLATES = str(Path(__file__).resolve().parent.parent / 'templates')
templates = Jinja2Templates(directory=PATH_TEMPLATES)

@router.get("/", response_class=HTMLResponse)
async def get(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})

@router.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        await websocket.send_text(f"Message text was: {data}")