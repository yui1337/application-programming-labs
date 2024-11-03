import argparse

from image_processing import *


def get_args() -> tuple[str, str]:
    """
    Reads arguments from terminal
    :return: Arguments
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--image_path", type=str, help="Path to the image you'd like to invert")
    parser.add_argument("-s", "--save_dir", type=str, help="Directory you'd like to save inverted image")
    arguments = parser.parse_args()
    return arguments.image_path, arguments.save_dir


def main():
    img_path, save_dir = get_args()
    try:
        img = get_image(img_path)
        print(get_image_dimensions(img))
    except Exception:
        print("Cant read image. Check your input.")
        exit()
    if img is not None:
        r_hist, g_hist, b_hist = make_histogram(img)
        draw_histogram(r_hist, g_hist, b_hist)
        inv_img = make_inverted_image(img)
        try:
            save_image(save_dir, inv_img)
        except Exception as e:
            print(f"Something went wrong:{e}. Try to input path that ends with '.YYY', where YYY - format of images")
        show_two_images(img, inv_img)
        plt.show()
    else:
        print("Something went wrong. Can't process image.")
        exit()


if __name__ == "__main__":
    main()
