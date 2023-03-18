import os
import sys
from loguru import logger


def runserver_uvicorn():
    logger.info('Uvicorn_server started')
    os.system('uvicorn main:app --reload ')
    
if __name__ == '__main__':
    command= " ".join( sys.argv[1:] )
    command_mapping = {
        'runserver': runserver_uvicorn,
    }
    command_mapping.get(command, lambda: logger.error(f'Unknown command: {command}'))()