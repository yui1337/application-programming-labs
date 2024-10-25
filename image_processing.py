import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

import os


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

def make_histogram(img: np.ndarray) -> None:
    """
    Creates histogram of given image and draws it
    :param img: Image in form of numpy array
    """
    channels = cv.split(img)
    colors = ["r", "g", "b"]

    plt.figure()
    plt.title("Histogram of original image")
    plt.xlabel("Brightness")
    plt.ylabel("Number of Pixels")

    for (channel, color) in zip(channels, colors):
        # create a histogram for the current channel and plot it
        histogram = cv.calcHist([channel], [0], None, [256], [0, 256])
        plt.plot(histogram, color=color)
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

def save_inverted_image(save_dir: str, img: np.ndarray, filename: str) -> None:
    """
    Saves image with inverted colors as jpeg file
    :param save_dir: Directory to save image
    :param img: Image in form of numpy array
    :param filename: Name of saved image without extension
    :return:
    """
    if not (os.path.isdir(save_dir)):
        os.mkdir(save_dir)
    filename = filename + ".jpg"
    save_dir = os.path.join(save_dir, filename)
    cv.imwrite(save_dir, img)


