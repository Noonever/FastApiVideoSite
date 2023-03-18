from random import choice, choices
from string import ascii_uppercase
import orjson
from loguru import logger
from settings import *


def video_is_being_processed(code: str) -> bool:
    return REDIS_CLIENT.hexists(REQUEST_QUEUE_HASH, code)


def video_is_stored(code: str) -> bool:
    return REDIS_CLIENT.sismember(VIDEO_CODES_SET, code)


def get_video_status(code: str) -> int:
    """
    Returns a video status by video code.
    """
    if video_is_being_processed(code):
        return 2
    elif video_is_stored(code):
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


def get_random_video_path() -> Path:
    video_paths = list(SOURCE_VIDEO_DIR.rglob("*.mp4"))
    random_path = choice(video_paths)
    return random_path.absolute()


def get_random_phrase() -> str:
    with open(PHRASES_FILE, "rb") as f:
        phrase = choice(orjson.loads(f.read()))
    return phrase


def create_generation_request(name: str) -> str:
    """
    Creates video generation request and returns its code
    """
    code = genetate_unique_code()
    text = f"{name.capitalize()}, {get_random_phrase()}"
    video_path = get_random_video_path()

    REDIS_CLIENT.rpush(REQUEST_QUEUE_LIST, code)
    REDIS_CLIENT.hset(REQUEST_QUEUE_HASH, code, f"{text}[,!,]{video_path}")
    # "[,!,] is used for splitting string in video processing program"
    return code


# Testing
# code_list = []
# while True:
#     command = input("command:")
#     if command == "st":
#         for code in code_list:
#             logger.info(f"Code: {code}, status: {get_video_status(code)}")
#     elif command =="red":
#         logger.debug(f"Generated: {REDIS_CLIENT.smembers(VIDEO_CODES_SET)}")
#         logger.debug(f"Queue: {REDIS_CLIENT.llen(REQUEST_QUEUE_LIST)}")
#         logger.debug(f"Queue hash: {REDIS_CLIENT.hgetall(REQUEST_QUEUE_HASH)}")
#     else:
#         new_code = create_generation_request(command)
#         code_list.append(new_code)

