import matplotlib.pyplot as plt
import pandas as pd

from img_operations import *

def make_df(csv_path: str) -> pd.DataFrame:
    """
    Creates pandas DataFrame from csv file
    :param csv_path: Path to the csv file
    :return: pandas DataFrame
    """
    df = pd.read_csv(csv_path, names=["rel_path", "abs_path"])
    df.drop(0, inplace=True)
    return df

def add_new_columns(df: pd.DataFrame) -> None:
    """
    Adds columns that contain width, height and number of channels of
    images in dataframe
    :param df: pandas DataFrame
    """
    height, width, channels = [],[],[]
    for i in range (1, len(df)+1):
        img = get_image(df.loc[i, "abs_path"])
        width.append(get_image_dimensions(img)[0])
        height.append(get_image_dimensions(img)[1])
        channels.append(get_image_dimensions(img)[2])
    df["width"] = width
    df["height"] = height
    df["channels"] = channels