from fastapi import APIRouter
from fastapi.responses import PlainTextResponse

router = APIRouter(
    prefix="/codespace",
    tags=["codespace endpoint"],
)

@router.get("/raw", response_class=PlainTextResponse)
async def test_route():
    ...


@router.get("/code_info")
async def test_route():
    ...