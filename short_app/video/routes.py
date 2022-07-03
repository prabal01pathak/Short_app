"""
Description: create, upload, view routes
Author: Prabal Pathak
"""
from fastapi import APIRouter, UploadFile

from .utils import write_file


router = APIRouter()


@router.post("/upload")
def upload(file: UploadFile) -> dict:
    """upload the video

    Args:
        file (UploadFile): video file

    Returns:
        dict : acknowledgement
    """
    ack = write_file(file)
    return ack
