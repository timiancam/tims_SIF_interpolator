import pathlib

def create_difference_csv(dataframe, type):
    parent_path = pathlib.Path(__file__).resolve().parent.parent.parent

    filename = 'difference_check_' + type + '_results.csv'
    
    path = pathlib.PurePath.joinpath(parent_path, filename)

    dataframe.to_csv(path, index=False)
