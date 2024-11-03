import argparse
import pandas as pd

from pandas_operations import *


def get_args() -> str:
    """
    Reads arguments from terminal
    :return: Arguments

    """
    parser = argparse.ArgumentParser()
    parser.add_argument("-c", "--csv", type=str, help="Path to the csv annotation")
    arguments = parser.parse_args()
    return arguments.csv

def main() -> None:
    csv_path = get_args()
    df = make_df(csv_path)



if __name__ == "__main__":
    main()
