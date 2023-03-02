from pathlib import Path

BASE_DIR = Path(__file__).resolve(strict=True).parent

SOURCE_VIDEO_DIR = BASE_DIR / 'media/source_videos'
SOURCE_VIDEO_DATA = SOURCE_VIDEO_DIR/'data.json'

PROCESSED_VIDEO_DIR = BASE_DIR / 'media/processed_videos'
PROCESSED_VIDEO_DATA = PROCESSED_VIDEO_DIR/'data.json'
