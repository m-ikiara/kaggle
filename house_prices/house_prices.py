"""House Prices - Advanced Regression Techniques.

Description:
    Ask a home buyer to describe their dream house, and they probably won't
    begin with the height of the basement ceiling or the proximity to an
    east-west railroad. But this playground competition's dataset proves that
    much more influences price negotiations than the number of bedrooms or a
    white-picket fence.
    With 79 explanatory variables describing (almost) every aspect of
    residential homes in Ames, Iowa, this competition challenges you to
    predict the final price of each home.
"""
import numpy as np
import pandas as pd


data = {
    'train_data': pd.read_csv("/kaggle/input/titanic/train.csv"),
    'test_data': pd.read_csv("/kaggle/input/titanic/test.csv"),
}


def display_data():
    """Output the data contained in file."""
    for k in data:
        data[k].head()
