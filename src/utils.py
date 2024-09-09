import pandas as pd
import numpy as np
from scipy.stats import zscore 

def missing_values_table(df):
    # total missing values
    mis_val = df.isnull().sum()

    # percentage of missing value
    mis_val_percent = 100 * df.isnull().sum() / len(df)
 
    # dtype of missing value
    mis_val_type = df.dtypes

    # make a table with the results
    mis_val_table = pd.concat([mis_val, mis_val_percent, mis_val_type], axis=1)

    # rename the columns
    mis_value_table_ren_columns = mis_val_table.rename(columns={0: 'mis_val', 1: '% of Total Values', 2: 'Dtype'})

    # sort the table by percentage of missing descending
    mis_value_table_ren_columns = mis_value_table_ren_columns[mis_value_table_ren_columns.iloc[:, 1] != 0].sort_values('% of Total Values', ascending=False).round(1)   
 
    # print some summary information
    print("Your selected dataframe has " + str(df.shape[1]) + " columns\n"
        "There are " + str(mis_value_table_ren_columns.shape[0]) + " columns that have missing values.")

    # return the dataframe with missing information
    return mis_value_table_ren_columns


def connvert_bytes_to_megabytes(df, bytes_data):
    megabytes = 1 * 10**6 
    df[bytes_data] = df[bytes_data] / megabytes
    return df[bytes_data]


def fix_outlier(df, column):
    df[column] = np.where(df[column] > df[column].quantile(0.95), df[column].median(), df[column])
    return 

def remove_outliers(df, column_to_process, z_threshold=3):
    # apply outlier removal to the sortified column
    z_scores = zscore(df[column_to_process])
    outlier_column = column_to_process + "_Outlier"
    df[outlier_column] = (np.abs(z_scores) > z_threshold).astype(int)
    df = df[df[outlier_column] == 0]

    # drop the outlier column
    df = df.drop(columns=[outlier_column], errors='ignore')

    return df
