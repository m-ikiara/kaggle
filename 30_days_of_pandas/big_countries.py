"""30 Days of Pandas.

~~~~BiG CoUnTrIeS~~~~
Consider the Table below:
    +-------------+---------+
    | Column Name | Type    |
    +-------------+---------+
    | name        | varchar | +=====> Primary Key
    | continent   | varchar |
    | area        | int     |
    | population  | int     |
    | gdp         | bigint  |
    +-------------+---------+

Each row of this table gives information about the name of a country, the
continent to which it belongs, its area, the population, and its GDP value.

A country is considered big if it has:
    1. an area of at least three million (i.e., 3000000 km2), or
    2. a population of at least twenty-five million (i.e., 25000000).

You are tasked with writing a solution to find the name, population, and area
of the big countries and return the result table in any order.

Example:
    Input: world = pd.DataFrame
        +-------------+-----------+---------+------------+--------------+
        | name        | continent | area    | population | gdp          |
        +-------------+-----------+---------+------------+--------------+
        | Afghanistan | Asia      | 652230  | 25500100   | 20343000000  |
        | Albania     | Europe    | 28748   | 2831741    | 12960000000  |
        | Algeria     | Africa    | 2381741 | 37100000   | 188681000000 |
        | Andorra     | Europe    | 468     | 78115      | 3712000000   |
        | Angola      | Africa    | 1246700 | 20609294   | 100990000000 |
        +-------------+-----------+---------+------------+--------------+
    Output: result = pd.DataFrame
        +-------------+------------+---------+
        | name        | population | area    |
        +-------------+------------+---------+
        | Afghanistan | 25500100   | 652230  |
        | Algeria     | 37100000   | 2381741 |
        +-------------+------------+---------+
"""
import pandas as pd


def big_countries(world: pd.DataFrame) -> pd.DataFrame:
    """Return the Statistics of the Big Countries.

    Args:
        world ('obj': pd.DataFrame): A Table of the World's Countries

    Returns:
        result ('obj': pd.DataFrame): The required Statistics.
    """
    result = world.loc[
            (world["population"] >= 25000000) | (world["area"] >= 3000000)]
    return result[["name", "population", "area"]]
