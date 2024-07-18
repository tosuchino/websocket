from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
import uvicorn

from app.routers import router_home, router_progress

def add_routers(app: FastAPI) -> None:
    app.include_router(router_home.router)
    app.include_router(router_progress.router)

app = FastAPI()

add_routers(app)

if __name__ == "__main__":
    uvicorn.run("app.main:app",
                port=8000,
                host="0.0.0.0",
                reload=True)