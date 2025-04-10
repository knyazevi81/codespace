from fastapi import APIRouter, Depends, Form
from fastapi.responses import PlainTextResponse

from src.users.dependecies import get_current_user
from src.users.models import Users
from src.codespace.service import CodespaceService
from src.codespace.utils import generate_uuid


router = APIRouter(
    tags=["Codespace endpoint"],
)


@router.post("/upload")
async def test_route(
    code_text: str = Form(..., description="The code text to upload"),
    project_name: str = Form(..., description="Project name"),
    public_access: bool = Form(..., description="public or private access"),
    user: Users = Depends(get_current_user)
):
    code_space_uuid = await generate_uuid()

    await CodespaceService.add(
        project_name=project_name,
        code=code_text,
        public_access=public_access,
        uuid=code_space_uuid,
        user_id=user.id
    )
    return code_space_uuid    


@router.get("/raw/{codespace_uuid}", response_class=PlainTextResponse)
async def test_route(
    codespace_uuid: str
):
    res = await CodespaceService.find_one_or_none(
        uuid=codespace_uuid
    )
    return res.code