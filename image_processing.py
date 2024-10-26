import os

import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np


def get_image(image_path: str) -> np.ndarray:
    """
    Reads image from given file
    :param image_path: Path to the image
    :return: Image in form of numpy array
    """
    img = cv.imread(image_path)
    img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    return img

def get_image_dimensions(img: np.ndarray) -> str:
    """
    Returns image dimensions
    :param img: Image in form of numpy array
    :return: string with image sizes
    """
    width, height = img.shape[1], img.shape[0]
    result = f"Image sizes (width, height) are: {width} x {height} px"
    return result

def make_histogram(img: np.ndarray) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """
    Creates RGB histogram of image given in from of numpy array
    :param img: Image in form of numpy array
    :return: Red, blue and green histograms
    """
    r_hist = cv.calcHist([img], [0], None, [256], [0, 256])
    g_hist = cv.calcHist([img], [1], None, [256], [0, 256])
    b_hist = cv.calcHist([img], [2], None, [256], [0, 256])
    return r_hist, b_hist, g_hist

def draw_histogram(r_hist: np.ndarray, g_hist: np.ndarray, b_hist: np.ndarray) -> None:
    """
    Draws RGB histogram
    :param r_hist: Red channel of image
    :param g_hist: Red channel of image
    :param b_hist: Red channel of image
    """
    plt.figure()
    plt.title("Histogram of original image")
    plt.xlabel("Brightness")
    plt.ylabel("Number of Pixels")
    plt.plot(r_hist, color="red")
    plt.plot(g_hist, color="green")
    plt.plot(b_hist, color="blue")
    plt.xlim([0, 256])


def make_inverted_image(img: np.ndarray) -> np.ndarray:
    """
    Inverts colors of given image
    :param img: Image in form of numpy array
    :return: Image with inverted colors in form of numpy array
    """
    return cv.bitwise_not(img)

def show_two_images(img: np.ndarray, inv_img: np.ndarray) -> None:
    """
    Draws matplotlib figure with two images
    :param img: Original mage in form of numpy array
    :param inv_img: Image with inverted colors in form of numpy array
    """
    plt.figure()

    plt.subplot(2, 1, 1)
    plt.imshow(img)
    plt.title("Original image")
    plt.axis('off')

    plt.subplot(2, 1, 2)
    plt.imshow(inv_img)
    plt.title("Inverted image")
    plt.axis('off')

def save_image(save_dir: str, img: np.ndarray) -> None:
    """
    Saves image as jpeg file
    :param save_dir: Path to the directory and file name with certain to save image as
    :param img: Image in form of numpy array
    :return:
    """
    cv.imwrite(save_dir, img)


