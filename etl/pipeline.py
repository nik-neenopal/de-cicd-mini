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
    print("Running Extraction...")
    df = extract("data/input.csv")
    print("Running transformation...")
    df = transform(df)
    print("Running loading...")
    load(df, "data/output.csv")
    print("ETL process completed.")