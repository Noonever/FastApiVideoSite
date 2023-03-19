import os
import sys
from loguru import logger
from settings import SOURCE_VIDEO_DIR, PROCESSED_VIDEO_DIR, BIN_FILE_PATH

def start_video_processor():
    os.system(f'{BIN_FILE_PATH} {SOURCE_VIDEO_DIR} {PROCESSED_VIDEO_DIR}')

def runserver_uvicorn():
    logger.info('Uvicorn_server started')
    os.system('uvicorn main:app --reload ')
    
if __name__ == '__main__':
    command= " ".join( sys.argv[1:] )
    command_mapping = {
        'runserver': runserver_uvicorn,
        'startprocessor': start_video_processor
    }
    command_mapping.get(command, lambda: logger.error(f'Unknown command: {command}'))()