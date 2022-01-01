import os
from datetime import datetime
from PIL import Image

from get_exif_data import get_exif_item, EXIF_DATETIME_FORMAT


input_path = 'raw'
output_path = 'sorted'
unsorted_dir_name = "_unsorted"

SHORT_DATE_FORMAT = "%Y-%m-%d"


def processDir(dirPath):
    for dirEntry in os.scandir(dirPath):
        if dirEntry.is_dir():
            processDir(dirEntry.path)

        else:
            processFile(dirEntry)


def copyImage(image, dir, fileName):
    create_dir(dir)
    copy = image.copy()
    copy.save(dir + "/" + fileName)


def processFile(dirEntry):

    try:
        with Image.open(dirEntry.path) as image:
            # default directory is unsorted
            dir = output_path + "/" + unsorted_dir_name

            exif_DateTime = get_exif_item(image, "DateTime")  # exif ID 306

            # reset dir name if exif date exists
            if exif_DateTime:
                date = datetime.strptime(
                    exif_DateTime["value"], EXIF_DATETIME_FORMAT)

                dir = output_path + "/" + date.strftime(SHORT_DATE_FORMAT)

            copyImage(image, dir, dirEntry.name)

    except OSError:
        print("Not an Image File")
        pass


def create_dir(path):
    try:
        os.mkdir(path)
    except FileExistsError:
        pass


def main():
    print(f"Read from {input_path}")
    print(f"Copy To {output_path}")

    processDir(input_path)


if __name__ == "__main__":
    main()
