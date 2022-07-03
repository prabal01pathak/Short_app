"""
Description: utiltiez for video app
Author: Prabal Pathak
"""
import shutil
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
