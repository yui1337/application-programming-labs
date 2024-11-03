import pandas as pd

def make_df(csv_path: str) -> pd.DataFrame:
    df = pd.read_csv(csv_path)
    return df