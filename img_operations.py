import cv2 as cv
import numpy as np


def get_image(image_path: str) -> np.ndarray:
    """
    Reads image from given file
    :param image_path: Path to the image
    :return: Image in form of numpy array
    """
    img = cv.imread(image_path)
    #img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    return img


def get_image_dimensions(img: np.ndarray) -> tuple[int,int, int]:
    """
    Returns image dimensions and its channel count
    :param img: Image in form of numpy array
    :return: tuple of image sizes
    """
    width, height, channels = img.shape[1], img.shape[0], img.shape[2]
    return width, height, channels
