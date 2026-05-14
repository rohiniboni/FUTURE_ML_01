import pandas as pd

def load_and_clean_data(path):
    df = pd.read_csv(path)
    df = df.dropna()

    df['Discount Price'] = df['Discount Price'].replace('[₹,]', '', regex=True).astype(float)
    df['Actual Price'] = df['Actual Price'].replace('[₹,]', '', regex=True).astype(float)

    return df