import os
from cs50 import get_string


def get_directory(prompt):
    while True:
        path = get_string(prompt)
        if os.path.isdir(path):
            break
        else:
            print("This path does not lead to a valid directory.")

    return path
