import os
from datetime import datetime
from PIL import Image
from PIL.ExifTags import TAGS

inputPath = 'raw-photos'
outputPath = 'sorted-photos'
outputPath_unsorted = outputPath + '/_unsorted'

dateTime_format = "%Y:%m:%d %H:%M:%S"

tag_DateTime = 306
tag_DateTimeOriginal = 36867
tag_DateTimeDigitized = 36868
tag_PreviewDateTime = 50971


def processDir(dirPath):
    for dirEntry in os.scandir(dirPath):
        processDirEntry(dirEntry)


def processDirEntry(dirEntry):
    if dirEntry.is_dir():
        processDir(dirEntry.path)

    else:
        processFile(dirEntry)


def getExifDate(image):
    exifData = image.getexif()

    if exifData is None or len(exifData) == 0:
        # print('Sorry, image has no exif data.')
        return None

    for key, val in exifData.items():
        if key in [tag_DateTime]:
            return val


def processFile(dirEntry):
    print("============================")
    print(f"processFile {dirEntry.path}")

    try:
        with Image.open(dirEntry.path) as image:
            copy = image.copy()
            exifDate = getExifDate(image)

            if exifDate:
                date = datetime.strptime(exifDate, dateTime_format)

                try:
                    path = outputPath + \
                        "/" + date.strftime("%Y-%m-%d")
                    os.mkdir(path)
                    copy.save(path + "/" + dirEntry.name)

                except FileExistsError:
                    pass

                print(exifDate, date)

            else:
                # pass
                # unsorted
                copy.save(outputPath_unsorted + "/" + dirEntry.name)

    except OSError:
        print("Not an Image File")
        pass

    # info = dirEntry.stat()
    # print(f"processFile {dirEntry.path} {info}")
    # print(datetime.utcfromtimestamp(info.st_atime))
    # print(datetime.utcfromtimestamp(info.st_mtime))
    # print(datetime.utcfromtimestamp(info.st_ctime))


def main():
    print(f"Read from {inputPath}")
    print(f"Copy To {outputPath}")

    # Prepare outputDir
    try:
        os.mkdir(outputPath_unsorted)
    except FileExistsError:
        pass

    processDir(inputPath)

    # for tag in TAGS:
    #     if 'ext' in TAGS[tag].lower():
    #         print(tag, TAGS[tag])


if __name__ == "__main__":
    main()
