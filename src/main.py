from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from contextlib import asynccontextmanager

from src.codespace.router import router as code_space_router

from src.database import create_tables


@asynccontextmanager
async def lifespan(app: FastAPI):
    await create_tables()
    yield


def get_application() -> FastAPI:
    _app = FastAPI(
        title="savecode api",
    )

    _app.include_router(code_space_router)

    _app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"], #TODO add front
        allow_credentials=True,
        allow_methods=["GET", "POST", "DELETE", "PUT", "PATCH"],
        allow_headers=["Content-Type", "Set-Cookie", "Access-Control-Allow-Headers",
                       "Access-Control-Allow-Origin", "Authorization"],
    )
    return _app

app = get_application()
