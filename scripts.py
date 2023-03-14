from settings import PROCESSED_VIDEO_DIR, PROCESSED_VIDEO_DATA
import os
import sys
from loguru import logger


def delete_processed_videos():
    for filename in PROCESSED_VIDEO_DIR.glob('*.mp4'):
        filename.unlink()
    
    PROCESSED_VIDEO_DATA.unlink()
    with PROCESSED_VIDEO_DATA.open('w') as f:
        f.write('[]')
    logger.info('Processed videos deleted')

def runserver_uvicorn():
    logger.info('Uvicorn_server started')
    os.system('uvicorn main:app --reload ')
    
if __name__ == '__main__':
    command= " ".join( sys.argv[1:] )
    command_mapping = {
        'delete': delete_processed_videos,
        'runserver': runserver_uvicorn,
    }
    command_mapping.get(command, lambda: logger.error(f'Unknown command: {command}'))()