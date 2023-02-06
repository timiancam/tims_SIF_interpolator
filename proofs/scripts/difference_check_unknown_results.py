from difference_check_scripts.get_csvs import get_csvs
from difference_check_scripts.create_difference_dataframe import create_difference_dataframe
from difference_check_scripts.create_difference_csv import create_difference_csv

def main():
    python_results, excel_results = get_csvs('unknown')

    dataframe = create_difference_dataframe(python_results, excel_results)

    create_difference_csv(dataframe, 'unknown')
        
main()
