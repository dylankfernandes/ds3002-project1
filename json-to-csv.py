import os
import click
import pandas as pd
from pandas.io import json

@click.command()
@click.option('--file', help='The name of the JSON file to convert to CSV')
def json_to_csv(file):
    """Converts a JSON file to CSV"""

    # if a file isn't specified, exit
    if not file:
        print("Please specify a file!")
        return

    # if a file isn't in this dataset, exit
    if not os.path.exists(file):
        print('Please specify an existing file!')
        return

    # return an error if the specified file is not a JSON file
    if file.split('.')[-1] != 'json':
        print('Please provide a JSON file!')
        return

    filename = file.split('.')[0]
    csv_file = f"{filename}.csv"
    df = pd.read_json(file)
    df.to_csv(csv_file)

    print("Conversion complete!")

if __name__ == '__main__':
    json_to_csv()
