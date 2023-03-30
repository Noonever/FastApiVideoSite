from fastapi import FastAPI, Request, status
from fastapi.responses import HTMLResponse, FileResponse, RedirectResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from loguru import logger

from settings import VIDEO_DIR

from services import is_page_exists, create_page, get_page_data

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")


@app.post("/create-page/{name}")
async def create(name: str):
    code = create_page(name=name)
    return RedirectResponse(url=f'/{code}', status_code=status.HTTP_303_SEE_OTHER)


@app.get('/video/{video_id}', response_class=FileResponse)
async def get_video(video_id: str):
    logger.info(f'Video {video_id} requested.')
    return f"{VIDEO_DIR}/{video_id}.mp4"


@app.get("/", response_class=HTMLResponse)
async def main_page(request: Request):
    logger.info(f'Main page visited. Visitor: {request.client.host}')
    return templates.TemplateResponse("main_template.html", {"request": request})


@app.get('/{code}', response_class=HTMLResponse)
async def get_video_page(request: Request, code: str):
    if is_page_exists(code=code):
        video_id, name, phrase = get_page_data(code=code)
        logger.info(f"Video page {code} visited. Visitor: {request.client.host}")
        context = {"request": request, "code": code, "video_id": video_id, "name": name, "phrase": phrase}
        return templates.TemplateResponse("video_template.html", context)
    else:
        logger.info(f"Video page with invalid code: {code} visited. Redirecting to main page")
        return RedirectResponse(url='/')