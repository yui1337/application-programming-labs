import argparse
import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

from image_processing import *

def get_args() -> tuple[str, str, str]:
    """
    Reads arguments from terminal
    :return: Arguments
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--image_path", type=str, help="Path to the image you'd like to invert")
    parser.add_argument("-s", "--save_dir", type=str, help="Directory you'd like to save inverted image")
    parser.add_argument("-n", "--new_filename", type=str, help="Name of inverted image")
    arguments = parser.parse_args()
    return arguments.image_path, arguments.save_dir, arguments.new_filename


def main():
    img_path, save_dir, new_filename = get_args()

    img = get_image(img_path)
    print(get_image_dimensions(img))

    make_histogram(img)
    inv_img = make_inverted_image(img)
    save_inverted_image(save_dir, inv_img, new_filename)
    show_two_images(img,inv_img)
    plt.show()

if __name__ == "__main__":
    main()
