import pandas as pd
import numpy as np

# Calculation of mean target per category for target encoding
def calc_target_encoding(df, cat_col, target_col):
    target_mean = df.groupby(cat_col)[target_col].mean()
    return target_mean
