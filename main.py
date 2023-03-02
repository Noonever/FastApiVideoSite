from fastapi import FastAPI, Request, status
from fastapi.responses import HTMLResponse, FileResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from loguru import logger

from settings import PROCESSED_VIDEO_DIR

from services import video_exisits, create_video

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def main_page(request: Request):
    logger.info(f'Main page visited. Visitor: {request.client.host}')
    return templates.TemplateResponse("main_template.html", {"request": request})


@app.post("/generate/{name}")
async def generate_request(name: str):
    code = create_video(name)
    return RedirectResponse(url=f'/{code}', status_code=status.HTTP_303_SEE_OTHER)


@app.get('/{code}', response_class=HTMLResponse)
async def video_page(request: Request, code: str):
    if video_exisits(code):
        logger.info(f"Video page {code} visited. Visitor: {request.client.host}")
        return templates.TemplateResponse("video_template.html", {"request": request, "code": code})
    else:
        return RedirectResponse(url='/')


@app.get('/video/{code}', response_class=FileResponse)
async def get_video(code: str):
    logger.info(f'Video {code} requested.')
    return f"{PROCESSED_VIDEO_DIR}/{code}.mp4"

