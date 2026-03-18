import pandas as pd

def extract(path):
    return pd.read_csv(path)

def transform(df):
    df = df.dropna()
    df["total"] = df["quantity"] * df["price"]
    return df

def load(df, output_path):
    df.to_csv(output_path, index=False)

if __name__ == "__main__":
    df = extract("data/input.csv")
    df = transform(df)
    load(df, "data/output.csv")