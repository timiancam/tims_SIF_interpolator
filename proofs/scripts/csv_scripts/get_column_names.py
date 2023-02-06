import csv
from csv_scripts.get_column_name_csv import get_column_name_csv

def get_column_names():
    with open(get_column_name_csv()) as csvfile:
        csv_reader = csv.reader(csvfile, delimiter=',')

        for row in csv_reader:
            column_names = row
    
    return column_names
    