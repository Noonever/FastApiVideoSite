from pathlib import Path


BASE_DIR = Path(__file__).resolve(strict=True).parent
VIDEO_DIR = BASE_DIR / "media"
VIDEO_DATA_FILE = VIDEO_DIR / "video_data.json"

# Name of redis storage
STORED_PAGES_HASH = "pages"