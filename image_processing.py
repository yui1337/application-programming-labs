import cv2 as cv


def open_image(image_path: str):
    img = cv.imread(image_path)
    return img

def print_image_dimensions(img) -> str:
    width, height  = img.shape[1], img.shape[0]
    result = f"Image sizes (width, height) are: {width} x {height}"
    return result