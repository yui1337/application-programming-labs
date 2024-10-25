import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np


def get_image(image_path: str) -> np.ndarray:
    img = cv.imread(image_path)
    img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    return img

def get_image_dimensions(img: np.ndarray) -> str:
    width, height = img.shape[1], img.shape[0]
    result = f"Image sizes (width, height) are: {width} x {height} px"
    return result

def make_histogram(img: np.ndarray) -> None:
    channels = cv.split(img)
    colors = ["r", "g", "b"]

    plt.figure()
    plt.title("'Flattened' Color Histogram")
    plt.xlabel("Bins")
    plt.ylabel("# of Pixels")

    for (channel, color) in zip(channels, colors):
        # create a histogram for the current channel and plot it
        histogram = cv.calcHist([channel], [0], None, [256], [0, 256])
        plt.plot(histogram, color=color)
        plt.xlim([0, 256])




