from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from contextlib import asynccontextmanager
from fastapi.staticfiles import StaticFiles

from src.database import create_tables
from src.codespace.router import router as code_space_router
from src.users.router import router as users_router
from src.frontend.router import router as frontend_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    await create_tables()  # Создаем Базу
    yield


def get_application() -> FastAPI:
    _app = FastAPI(title="savecode api", lifespan=lifespan)

    _app.mount("/static", StaticFiles(directory="src/frontend/public/static"), "static")

    _app.include_router(code_space_router)
    _app.include_router(users_router)
    _app.include_router(frontend_router)

    _app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],  # TODO add front
        allow_credentials=True,
        allow_methods=["GET", "POST", "DELETE", "PUT", "PATCH"],
        allow_headers=[
            "Content-Type",
            "Set-Cookie",
            "Access-Control-Allow-Headers",
            "Access-Control-Allow-Origin",
            "Authorization",
        ],
    )
    return _app


app = get_application()
