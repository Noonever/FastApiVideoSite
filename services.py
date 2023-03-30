from random import choice, choices
from string import ascii_uppercase
import orjson
from settings import *
import redis


REDIS_CLIENT = redis.Redis(host='localhost', port=6379, db=0)


def is_page_exists(code: str):
    return REDIS_CLIENT.hexists(STORED_PAGES_HASH, code)


def genetate_unique_code() -> str:
    """
    Generates and returns a unique code for a new page
    """
    length = 6

    while True:
        code = ''.join(choices(ascii_uppercase, k=length))
        if not is_page_exists(code=code):
            break

    return code


def get_random_video_id() -> int:
    pass


def get_video_phrase(video_id: int):
    pass


def create_page(name: str) -> str:
    """
    Creates a page with a unique code and writes its data to redis
    """
    code = genetate_unique_code()
    video_id = get_random_video_id()
    data_string = f"{video_id}[,!,]{name}"
    REDIS_CLIENT.hset(STORED_PAGES_HASH, code, data_string)
    return code


def get_page_data(code: str) -> tuple[int, str, str]:
    """
    Returns a tuple of video_id, name, phrase
    """
    data = REDIS_CLIENT.hget(STORED_PAGES_HASH, code)
    video_id, name = data.split("[,!,]")
    phrase = get_video_phrase(video_id=video_id)
    return video_id, name, phrase


