import os
import click
import pandas as pd
from pandas.io import json

@click.command()
@click.option('--file', help='The name of the CSV file to convert to JSON')
def csv_to_json(file):
    """Converts a CSV file to JSON"""

    # if a file isn't specified, exit
    if not file:
        print("Please specify a file!")
        return

    # if a file isn't in this dataset, exit
    if not os.path.exists(file):
        print('Please specify an existing file!')
        return

    # return an error if the specified file is not a JSON file
    if file.split('.')[-1] != 'csv':
        print('Please provide a CSV file!')
        return

    filename = file.split('.')[0]
    json_file = f"{filename}.json"
    df = pd.read_csv(file)
    df.to_json(json_file)

    print("Conversion complete!")

if __name__ == '__main__':
    csv_to_json()