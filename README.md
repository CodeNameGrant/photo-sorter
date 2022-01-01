# Photo-Sorter

A simple app to copy images from one dir to anohter and group them by the date they were taken.
This is determined from the image meta data no the file name.

## Run Locally

```bash
  git clone https://github.com/CodeNameGrant/photo-sorter.git
  pip3 install -r requirements. txt
  python app.js
```

You will then be asked to enter the input/output directories. Rather use abolute paths, starting from your root directory otherwise they will be interpreted as reletive to `app.js`

## Acknowledgements

- [How to Extract Image Metadata in Python](https://www.thepythoncode.com/article/extracting-image-metadata-in-python)
- [Python Pillow Library](https://github.com/python-pillow/Pillow/tree/40e7ff622669550733b26f14dc817fb72e096250)
- [CS50 Python Library](https://github.com/cs50/python-cs50)

## Authors

- [@CodeNameGrant](https://github.com/CodeNameGrant)
