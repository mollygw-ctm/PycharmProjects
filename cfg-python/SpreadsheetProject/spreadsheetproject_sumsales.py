import pandas as pd
import numpy as np

def sumsales():
    df = pd.read_csv('sales.csv')

    sum_row=df["sales"].sum()
    print(sum_row)

sumsales()