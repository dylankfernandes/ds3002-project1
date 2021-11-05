import click
import pyfiglet as pfg

class Color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

@click.command()
def welcome():
    print(f"{Color.GREEN}{pfg.figlet_format('Welcome to ETL!')}{Color.END}")
    print(f"This project includes a forest cover dataset for demo purposes, but{Color.DARKCYAN} any csv-based dataset{Color.END} can be used by this ETL pipeline. \n")
    print("There are four primary functions provided by the ETL Pipeline, which can be triggered by running python <file>.py")
    print(f" *{Color.GREEN} add-column.py{Color.END} - adds a column which just fills the column with a single value; unless specified by you, both the name and column values default to 'Tree' and 'Leaf', respectively.")
    print(f" *{Color.GREEN} summarize.py{Color.END} - summarizes the dataset, including the number of rows, columns, dataset statistics, and even a preview of the dataset itself; you can view shortened version of this version by turning verbose mode off.")
    print(f" *{Color.GREEN} csv-to-json.py{Color.END} - converts a csv dataset to json; you can specify the dataset you want to convert as a flag.")
    print(f" *{Color.GREEN} json-to-csv.py{Color.END} - converts a json dataset to csv; you can specify the dataset you want to convert as a flag.")
    print(f"\nTo understand how each function can be called, you can use the {Color.DARKCYAN}--help{Color.END} flag when running any of these scripts.\n")

if __name__ == '__main__':
    welcome()