from pathlib import Path
import threading
import queue

from fastapi import APIRouter, WebSocket
from fastapi.requests import Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from app.lib.count import count_num

router = APIRouter()

PATH_TEMPLATES = str(Path(__file__).resolve().parent.parent / 'templates')
templates = Jinja2Templates(directory=PATH_TEMPLATES)

@router.get("/progress", response_class=HTMLResponse)
async def get():
    return templates.TemplateResponse("home.html", {"request": request})

@router.get("/calc")
def calc_get(request: Request):
    return templates.TemplateResponse("calc.html", {"request": request})

@router.post("/calc")
def calc_get(request: Request):
    return templates.TemplateResponse("calc.html", {"request": request})

@router.get("/thread")
def thread_start():
    q = queue.Queue()
    print(q.empty())
    worker_thread = threading.Thread(target=count_num, args=(q, ))
    worker_thread.start()
    print(q.empty())
    print(q.get())