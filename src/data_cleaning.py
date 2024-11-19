import pandas as pd
import numpy as np

def missing_values_table(df):
    missing_values = df.isnull().sum()
    missing_percent = 100 * missing_values / len(df)
    return pd.DataFrame({'Missing Values': missing_values, 'Percent': missing_percent}).sort_values(by='Percent', ascending=False)

def fix_outliers(df, column, method='median', threshold=3):
    if method == 'median':
        cap_value = df[column].quantile(0.95)
        df[column] = np.where(df[column] > cap_value, cap_value, df[column])
    elif method == 'zscore':
        mean, std = df[column].mean(), df[column].std()
        z_scores = (df[column] - mean) / std
        df = df[z_scores.abs() <= threshold]
    return df

def convert_bytes_to_mb(df, columns):
    for col in columns:
        df[col] = df[col] / (1024 * 1024)
    return df
