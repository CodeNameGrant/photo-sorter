# -----------------------------------------------------
#
# Utility library to extract exif data for PIL Image objects in various ways
#
# -----------------------------------------------------

from os import error
from typing import Optional

from PIL import Image
from PIL.ExifTags import TAGS

EXIF_DATETIME_FORMAT = "%Y:%m:%d %H:%M:%S"


def get_exif_data(image: Image) -> dict:
    """
    Uses PIL Image.getexif() to extract exif data. 

    Consistently returns a blank dict of there is no exif data
    """

    exifData = image.getexif()

    if exifData is None or len(exifData) == 0:
        return {}

    return exifData


def get_exif_dict_list(image: Image) -> list:
    """
    Enhances the exif data with each items tag

    Returns a list of dict objects, structured as follows: { id, tag, value }
    """

    exifData = get_exif_data(image)

    exifList = []

    try:
        for key, val in exifData.items():
            exifList.append({
                "id": key,
                "tag": TAGS[key],
                "value": val
            })

    except:
        # Ignore unknown exif ids
        pass

    return exifList


def get_exif_item(image: Image, field: int | str) -> Optional[dict]:
    """
    Searches the Image for a specific exif item either by id or (exact) string

    Returns a single exif item enhanced by get_exif_dict_list() or None
    """

    exifDict = get_exif_dict_list(image)
    if exifDict == None:
        return None

    for item in exifDict:
        if item["id"] == field or item["tag"] == field:
            return item

    return None
