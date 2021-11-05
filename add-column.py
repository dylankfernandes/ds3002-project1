import pandas as pd
import click
import os

@click.command()
@click.option('--file', help='The name of the dataset to add the new column to (CSV only)')
@click.option('--name', default='Tree', help='The name of the new column')
@click.option('--value', default='Leaf', help='The value to fill the new column with')
@click.option('--overwrite', default=False, help='If a column with this name already exists, you can use this flag to overwrite that column.')
def add_column(file, name, value, overwrite):
    """Adds a new column filled with a single value, and rewrite the file to disk."""

    # if a file isn't specified, exit
    if not file:
        print("Please specify a file!")
        return

    # if a file isn't in this dataset, exit
    if not os.path.exists(file):
        print('Please specify an existing file!')
        return

    # return an error if the specified file it's not a CSV file
    if file.split('.')[-1] != 'csv':
        print('Please provide a CSV file!')
        return

    # read the dataset
    df = pd.read_csv(file)

    # if a column already exists in the dataset, check if we're allowed to overwrite it
    if name in df.columns:
        if not overwrite:
            print('Attempted to overwrite a column without explicit permisison. Exiting...')
            return

    # write the new column to disk    
    df[str(name)] = pd.Series([str(value)] * len(df))
    df.to_csv(file)

if __name__ == '__main__':
    add_column()