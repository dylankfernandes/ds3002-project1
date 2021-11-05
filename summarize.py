import click
import pandas as pd
import os

@click.command()
@click.option('--file', help='The name of the file to summarize')
@click.option('--verbose', default=True, help='Enable verbose mode')
def generate_summary(file, verbose):
    """Summarize a CSV dataset"""

    # if a file isn't specified, exit
    if not file:
        print("Please specify a file!")
        return

    # if a file isn't in this dataset, exit
    if not os.path.exists(file):
        print('Please specify an existing file!')
        return

    # read the dataset from the file (error if it's not a CSV)
    if file.split('.')[-1] != 'csv':
        print('Please provide a CSV file!')
        return

    # read the dataset
    df = pd.read_csv(file)

    print('Dataset Summary')
    print('-------------------\n')

    print(f'Number of Rows: {len(df)}')
    print(f'Number of Columns: {len(df.columns)}\n')

    if verbose:
        print(f'Dataset Columns\n{", ".join(df.columns)}\n')
        print(f'Dataset Statistics\n{df.describe()}\n')
        print(f'Dataset Preview:\n{df.head()}\n')

if __name__ == '__main__':
    generate_summary()