from settings import PROCESSED_VIDEO_DIR, PROCESSED_VIDEO_DATA

# function that deletes all video_files from proceesed_video_dir and clears the data using pathlib
def clear_processed_video_dir():
    for filename in PROCESSED_VIDEO_DIR.glob('*.mp4'):
        filename.unlink()
    
    PROCESSED_VIDEO_DATA.unlink()
    with PROCESSED_VIDEO_DATA.open('w') as f:
        f.write('[]')

clear_processed_video_dir()

