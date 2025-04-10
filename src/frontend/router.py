from fastapi import APIRouter, Depends, Request, HTTPException
from fastapi.templating import Jinja2Templates

from fastapi.responses import RedirectResponse
from fastapi.middleware.httpsredirect import HTTPSRedirectMiddleware

from src.users.models import Users
from src.users.dependecies import get_current_user


router = APIRouter(
    tags=["frontend service"]
)

templates = Jinja2Templates("src/frontend/public")

#@router.get("/login")
#async def get_main(
#    request: Request, 
#    user: Users = Depends(get_current_user)
#):  
#    if user:
#        return templates.TemplateResponse(
#            "login.html",
#            {"request": request}
#        )



@router.get("/upload_code")
async def index(request: Request, user: Users = Depends(get_current_user)):
    if user:
        return templates.TemplateResponse("upload.html", {"request": request})    
    
