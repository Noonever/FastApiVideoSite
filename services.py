from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
from moviepy.editor import *

from loguru import logger
from random import choices
from string import ascii_uppercase
import json

from settings import *


def read_json(file_path):
    with open(file_path, 'r') as f:
        data = json.load(f)
    return data


def video_exisits(code: str):
    data = read_json(PROCESSED_VIDEO_DATA)
    return code in data


def add_video_to_data(code: str):
    data = read_json(PROCESSED_VIDEO_DATA)
    data.append(code)
    with open(PROCESSED_VIDEO_DATA, 'w') as f:
        json.dump(data, f, indent=4)
    logger.info(f'Video {code} added to data.')

def genetate_unique_code():

        length = 6

        while True:
            code = ''.join(choices(ascii_uppercase, k=length))
            if not video_exisits(code=code):
                break

        return code


def generate_video(text: str, code: str):

    processed_video_file_path = f'{PROCESSED_VIDEO_DIR}\\{code}.mp4'
    source_video_file_path = f'{SOURCE_VIDEO_DIR}\\test.mp4'
    text_name = text.lower().capitalize() + ','
    text_to_input = text_name + " hello!"

    clip = VideoFileClip(source_video_file_path)

    txt_clip = TextClip(text_to_input, fontsize=110, color='red', font='Calibri-Bold', stroke_width=7, stroke_color='black')
    txt_clip = txt_clip.set_pos('center')

    fps = clip.fps

    final_clip = CompositeVideoClip([clip, txt_clip])
    final_clip.duration = clip.duration

    logger.info(f'Started clip generation with code: {code}, text: {text_to_input}.')

    final_clip.write_videofile(processed_video_file_path, fps=fps, threads=4, logger=None)

    logger.info(f'Clip {code} generated.')

def create_video(text: str):
    code = genetate_unique_code()
    generate_video(text=text, code=code)
    add_video_to_data(code=code)
    return code