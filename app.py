import os
from datetime import datetime
from PIL import Image

from get_exif_data import get_exif_item, EXIF_DATETIME_FORMAT


inputPath = 'raw-photos'
outputPath = 'sorted-photos'
unsorted_dir_name = "_unsorted"

unsorted_dir_path = outputPath + "/" + unsorted_dir_name

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
            copy = image.copy()
            exif_DateTime = get_exif_item(image, "DateTime")  # exif ID 306

            # default directory is unsorted
            dir = unsorted_dir_path

            # reset dir name if exif date exists
            if exif_DateTime:
                date = datetime.strptime(
                    exif_DateTime["value"], EXIF_DATETIME_FORMAT)

                dir = outputPath + "/" + date.strftime(SHORT_DATE_FORMAT)

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
    print(f"Read from {inputPath}")
    print(f"Copy To {outputPath}")

    processDir(inputPath)


if __name__ == "__main__":
    main()
