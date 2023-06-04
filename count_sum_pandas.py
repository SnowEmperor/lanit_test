import numpy
import pandas


def count_sum(df):
    res = df.groupby('Товар')['Количество'].sum()
    return res



