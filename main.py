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
    try:
        df = make_df(csv_path)
        print("DataFrame from csv \n", df)

        add_new_columns(df)
        print("Added width, height, channels columns \n", df)

        info = stat_info(df)
        print("Statistical information of DataFrame \n", info)

        filtered = filter_by_sizes(df, 1000, 1000)
        print("DataFrame filtered by max width, max_height \n", filtered)

        add_area(df)
        print("Added area column \n", df)

        sorted = sort_by_area(df)
        print("DataFrame sorted by area(from smaller to larger) \n", df)

        create_hist_by_area(df)
    except Exception as e:
        print(f"Something went wrong: {e}")


if __name__ == "__main__":
    main()
