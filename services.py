from random import choices
from string import ascii_uppercase
import orjson
from loguru import logger
from settings import *


def video_is_being_processed(code: str) -> bool:
    return REDIS_CLIENT.hexists(REQUEST_QUEUE_HASH, code)


def video_is_recently_created(code: str) -> bool:
    return REDIS_CLIENT.sismember(RECENT_VIDEOS_SET, code)


def video_is_stored(code: str) -> bool:
    with open(PROCESSED_VIDEO_DATA, 'rb') as f:
        stored_videos = orjson.loads(f.read())
    return code in stored_videos


def get_video_status(code: str) -> int:
    """
    Returns a video status by video code.
    """
    if video_is_being_processed(code):
        return 2
    elif video_is_recently_created(code) or video_is_stored(code):
        return 0
    else:
        return 1


def genetate_unique_code() -> str:
    """
    Generates and returns a unique code for a new video
    """
    length = 6

    while True:
        code = ''.join(choices(ascii_uppercase, k=length))
        video_status = get_video_status(code=code)
        if video_status == 1:
            break

    return code


def create_generation_request(text: str) -> str:
    """
    Returns code of a video
    """
    code = genetate_unique_code()
    REDIS_CLIENT.rpush(REQUEST_QUEUE_LIST, code)
    REDIS_CLIENT.hset(REQUEST_QUEUE_HASH, code, text)
    return code

# Testing
code_list = []
while True:
    command = input("command:")
    if command == "st":
        for code in code_list:
            logger.info(f"Code: {code}, status: {get_video_status(code)}")
    elif command =="red":
        logger.debug(f"Generated: {REDIS_CLIENT.smembers(RECENT_VIDEOS_SET)}")
        logger.debug(f"Queue: {REDIS_CLIENT.llen(REQUEST_QUEUE_LIST)}")
        logger.debug(f"Queue hash: {REDIS_CLIENT.hgetall(REQUEST_QUEUE_HASH)}")
    else:
        new_code = create_generation_request(command)
        code_list.append(new_code)
