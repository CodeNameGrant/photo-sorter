import os
from datetime import datetime

from cs50 import get_string
from PIL import Image

from get_exif_data import EXIF_DATETIME_FORMAT, get_exif_item
from utilities import get_directory

input_path = ""
output_path = ""
unsorted_dir_name = "_unsorted"


SHORT_DATE_FORMAT = "%Y-%m-%d"


def process_dir(dirPath):
    for dirEntry in os.scandir(dirPath):
        if dirEntry.is_dir():
            process_dir(dirEntry.path)

        else:
            process_file(dirEntry)


def copy_image(image, dir, fileName):
    create_dir(dir)
    copy = image.copy()
    copy.save(dir + "/" + fileName)


def process_file(dirEntry):
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

            copy_image(image, dir, dirEntry.name)

    except OSError:
        print("Not an Image File")
        pass


def create_dir(path):
    try:
        os.mkdir(path)
    except FileExistsError:
        pass


def main():
    global input_path
    global output_path

    input_path = get_directory(
        "Enter the directory where the unsorted photos are:\n")
    print("")

    output_path = get_string(
        "Enter the directory where sorted photos must be placed:\n")
    print("")

    print(f"Read from {input_path}")
    print(f"Copy To {output_path}")

    process_dir(input_path)

    print("Complete.")


if __name__ == "__main__":
    main()
