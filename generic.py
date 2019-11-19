import os


def check_and_create(path):
    """
    check if a directory exists. If not, create it
    :return:
    """
    if not os.path.exists(path):
        os.mkdir(path)