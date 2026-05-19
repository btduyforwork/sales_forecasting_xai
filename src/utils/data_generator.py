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

def correct_outliers(df,factor=3):
    corrected_df=df.copy()
    z_score=np.abs((corrected_df["sales"]-corrected_df["sales"].mean())/corrected_df["sales"].std())
    corrected_df.loc[z_score>factor,"sales"]=corrected_df["sales"].mean()
    return corrected_df