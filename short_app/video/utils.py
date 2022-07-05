"""
Description: helper functions for video app
Author: Prabal Pathak
"""
import shuti
from pathlib import Path
from fastapi import UploadFile


def write_file(file: UploadFile) -> dict:
    """write uploaded file

    Args:
        file (UploadFile): uploaded file

    Returns:
        dict: message
    """
    path = Path(f"upload/{file.filename}")
    with path.open("wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return {"message": "Uploaded succesfully", "file_name": file.filename}


async def get_video_list(cat: str):
    """ Return the available video list
    Args:
        cat(str): video category
    Return:
        video_dict(dict): available video dict
    """
    return {"1": "hi.mp4"}
