"""30 Days of Pandas.

~~~~Day 02: FIND PRODUCTS~~~~
Consider the Table below:
    +-------------+---------+
    | Column Name | Type    |
    +-------------+---------+
    | product_id  | int     | +=======> Primary Key
    | low_fats    | enum    | +=======> "Y" low in fat or "N" high in fat
    | recyclable  | enum    | +=======> "Y" recyclable or "N" non-recyclable
    +-------------+---------+

You are tasked with writing a solution to find the ids of products that are
both low fat and recyclable and return the result table in any order.

Example:
    Input: products = pd.DataFrame
        +-------------+----------+------------+
        | product_id  | low_fats | recyclable |
        +-------------+----------+------------+
        | 0           | Y        | N          |
        | 1           | Y        | Y          |
        | 2           | N        | Y          |
        | 3           | Y        | Y          |
        | 4           | N        | N          |
        +-------------+----------+------------+
    Output: result = pd.DataFrame
        +-------------+
        | product_id  |
        +-------------+
        | 1           |
        | 3           |
        +-------------+
"""
import pandas as pd


def find_products(products: pd.DataFrame) -> pd.DataFrame:
    """Return the recyclable Products that are Low in Fat.

    Args:
        products ('obj': pd.DataFrame): The various Product statistics

    Returns:
        result ('obj': pd.DataFrame): The required Data.
    """
    result = products.loc[
            (products["low_fats"] == "Y") & (products["recyclable"] == "Y")]
    return result[["product_id"]]
