import pandas as pd
import numpy as np
import argparse as ap


def parse_data(df: pd.DataFrame, value_to_search: str) -> pd.DataFrame:
    """
    Returns transformed DataFrame with averaged out data for each of 12 months for chosen city.

        Parameters:
            df (pandas DataFrame)
            value_to_search (string): name of the city

        Returns:
            data (pandas DataFrame): DataFrame with averaged out weather data for chosen city
    """
    try:

        df["date"] = pd.to_datetime(df.date, format="%Y-%m-%d")
        data = (
            df[df["name"] == value_to_search]
            .groupby(["name", df["date"].dt.to_period("M")])[["temp", "prcp", "wdsp"]]
            .agg(["mean"])
        )

    except ValueError as err:
        print(err.args)
    return data


def main() -> None:
    """
    Prints out transformed data for comparison. Can be run through CLI or in editor.
    """
    df = pd.read_csv("data.csv")
    grouped = df.groupby("name")
    stations = [key for key, _ in grouped]

    parser = ap.ArgumentParser(description="compare monthly city stats.")
    parser.add_argument("arg_a", help="name of first city", choices=stations)
    parser.add_argument("arg_b", help="name of second city", choices=stations)
    args = parser.parse_args()

    city_a = args.arg_a
    city_b = args.arg_b

    data = []
    if city_a and city_b in stations:
        data.append(parse_data(df, city_a))
        data.append(parse_data(df, city_b))

        connected_data = pd.concat(
            [data[1].xs(city_b), data[0].xs(city_a)], keys=[city_b, city_a], axis=1
        )

        temp_a = connected_data.iloc[:, 3]
        temp_b = connected_data.iloc[:, 0]

        city_a_temp_info = city_a.capitalize() + " was colder"
        city_b_temp_info = city_b.capitalize() + " was hotter"

        connected_data["hi/lo"] = np.where(
            temp_b >= temp_a, city_b_temp_info, city_a_temp_info
        )
        connected_data["temp_diff"] = np.where(temp_b == temp_a, 0, temp_b - temp_a)

        print(connected_data)


if __name__ == "__main__":
    main()
