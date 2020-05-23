"""
A module to provide some frequent functionalities for csv data in one place

Author: Faruk Ahmad
Date: 23 May, 2020
Ref: #
"""

# lets import the necessary stuffs
import pandas as pd


"""
A dummy method to read and get data frame from csv file
"""
def read_from_csv_simple(file_path):
    df = pd.read_csv(file_path)

    return df



"""
file_path: CSV file path to read
sep: custom value separator
dtype: parse specific columns using certain data types
usecols: pass column names to load from the csv file
parse_dates: interpret column as date type
skiprows: number of rows from top to skip while loading data
na_values: Replace mentioned values with NaN
"""
def read_from_csv_advanced(file_path, separators = ',', dytpes = {}, \
    usecols = [], parse_dates = [], skiprows = 0, na_values = []):
    data = pd.read_csv(
    file_path,
    sep = separators,
    dtype = dytpes, 
    usecols = usecols,
    parse_dates = parse_dates,
    skiprows = skiprows,
    na_values = na_values
    )

    return data



if __name__ == "__main__":
    file_path = './data.csv'
    data = read_from_csv_simple(file_path)
    print(f"Simpe read data: {data}")

    data = read_from_csv_advanced(file_path, usecols = ["name"])
    print(f"Advance read data: {data}")