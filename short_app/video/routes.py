"""
Description: create, upload, view routes
Author: Prabal Pathak
"""
from pathlib import Path

from fastapi import APIRouter, UploadFile
from fastapi.responses import FileResponse

from .utils import write_file, get_video_list


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


@router.post("/video_list")
async def video_list(cat: str):
    """Return available video list and there id's
    """
    return get_video_list(cat)


@router.get("/view")
async def view(_id: str):
    """View video file
    Args:
        id(str): video id
    Return:
        video
    """
    home_path = Path("/home/prabal/Downloads/")
    video_path = home_path / "PRG7.avi"
    print(_id)
    return FileResponse(video_path, media_type="video/mp4")
