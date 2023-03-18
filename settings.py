from pathlib import Path
import redis

BASE_DIR = Path(__file__).resolve(strict=True).parent

SOURCE_VIDEO_DIR = BASE_DIR / 'media/source_videos'
PROCESSED_VIDEO_DIR = BASE_DIR / 'media/processed_videos'
PHRASES_FILE = BASE_DIR / 'media/phrases.json'

REDIS_CLIENT = redis.Redis(host='localhost', port=6379, db=0)

# Names of redis storages
REQUEST_QUEUE_LIST = "generation_queue"
REQUEST_QUEUE_HASH = "generation_queue_data"
VIDEO_CODES_SET = "stored_video_codes"