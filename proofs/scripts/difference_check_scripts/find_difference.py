import pandas as pd

def find_difference(python_results, excel_results, column):
    
    raw_difference = python_results[column] - excel_results[column]
    abs_difference = abs(raw_difference)
    difference = abs_difference.round(3)

    return difference
