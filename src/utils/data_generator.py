import numpy as np
import pandas as pd

def check_missing_value(df):
    return pd.DataFrame(
        {
        "count": df.isna().sum(),
        "percentage": np.round(df.isna().sum() / len(df), 2) * 100
     }
)

def filling_missing_value_with_mean(df):
    df_coppy=df.copy()
    df_coppy["sales"]=df_coppy["sales"].fillna(df_coppy["sales"].mean())
    return df_coppy

def filling_missing_value_with_median(df):
    df_coppy=df.copy()
    df_coppy["sales"]=df_coppy["sales"].fillna(df_coppy["sales"].median())
    return df_coppy