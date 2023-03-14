from pathlib import Path
import redis

BASE_DIR = Path(__file__).resolve(strict=True).parent

SOURCE_VIDEO_DIR = BASE_DIR / 'media/source_videos'
SOURCE_VIDEO_DATA = SOURCE_VIDEO_DIR/'data.json'

PROCESSED_VIDEO_DIR = BASE_DIR / 'media/processed_videos'
PROCESSED_VIDEO_DATA = PROCESSED_VIDEO_DIR/'data.json'

REDIS_CLIENT = redis.Redis(host='localhost', port=6379, db=0)

# Names of redis storages
REQUEST_QUEUE_LIST = "generation_queue"
REQUEST_QUEUE_HASH = "generation_queue_hash"
RECENT_VIDEOS_SET = "recently_created_videos_set"