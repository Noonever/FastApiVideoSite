from fastapi import FastAPI
from fastapi.responses import HTMLResponse, FileResponse

from pathlib import Path

BASE_DIR = Path(__file__).resolve(strict=True).parent.parent
SOURCE_VIDEO_PATH = BASE_DIR / 'media/source_videos'
PROCESSED_VIDEO_PATH = BASE_DIR / 'media/processed_videos'

app = FastAPI()

