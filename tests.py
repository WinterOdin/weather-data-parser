from typing import NoReturn, Mapping
import pandas as pd
import numpy as np
import pytest
from script import parse_data


def load_csv() -> pd.DataFrame:
    """
    Compile data.csv into dataframe for the tests.
    """
    df = pd.read_csv("data.csv")
    return df


@pytest.fixture
def data_df_columns() -> list:
    """
    Get the columns of data.csv.
    """
    df_columns = load_csv().columns.tolist()
    return df_columns


@pytest.fixture
def dtype_df() -> Mapping:
    """
    Get the data types of the data.csv.
    """
    data_types = load_csv().dtypes.to_dict()
    return data_types


@pytest.fixture
def len_of_df() -> int:
    """
    Get length of original df.

    using len because is faster than shape
    """
    df_len = len(load_csv().index)
    return df_len


@pytest.fixture
def parsed_df() -> pd.DataFrame:
    """
    Creates new instance of transformed data using parse_data().
    """
    test_value = "LUBLIN"
    df_instance = parse_data(load_csv(), test_value)
    return df_instance


def tests_row_of_parsed_df(parsed_df: callable) -> NoReturn:
    """
    Test number of rows in parsed df.
    Expected number of rows is 12, one for each month.

    using len because is faster than shape
    """
    expected_num_row = 12
    assert len(parsed_df.index) == expected_num_row


def tests_cols_of_parsed_df(parsed_df: callable) -> NoReturn:
    """
    Test number of columns in parsed df.
    Expected number of columns is 5

    using len because is faster than shape
    """
    expected_num_col = 3
    assert len(parsed_df.columns) == expected_num_col


def test_of_df_len(len_of_df: callable) -> NoReturn:
    """
    Test length of df to be sure that data is loaded correctly.
    3629 - first row in csv is reserved for headers.
    """
    expected_row_number = 3629
    assert len_of_df == expected_row_number


def test_df_data_types(dtype_df: callable) -> NoReturn:
    """
    Test the data types of dataframe for potential database insertion.
    """
    schema_data_types = {
        "name": np.dtype("O"),
        "date": np.dtype("O"),
        "temp": np.dtype("int64"),
        "prcp": np.dtype("float64"),
        "wdsp": np.dtype("float64"),
    }

    assert dtype_df == schema_data_types


def test_if_columns_are_as_expected(data_df_columns: callable) -> NoReturn:
    """
    Test if the csv was transformed to dataframe
    without any lost columns.
    """
    schema_columns = ["name", "date", "temp", "prcp", "wdsp"]

    assert data_df_columns == schema_columns
