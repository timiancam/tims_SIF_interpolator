import numpy as np
import pathlib
import pandas as pd
import os
import json
import sys
from dotenv import load_dotenv
from scipy.interpolate import RegularGridInterpolator as rgi

def interpolate(inputs, geometry_defects):
    # .env file must be located in the same root directory as this script
    load_dotenv()
    
    geometry_defects = [defect.upper() for defect in geometry_defects]
    
    solution_keys = json.loads(os.environ.get('SOLUTION_KEYS'))

    interpolated_results = []
    
    interpolators = create_interpolator_dictionary(geometry_defects, solution_keys)
    
    for input_set in inputs:
        defect_solutions = {}
    
        for defect in geometry_defects:
            solutions = {}
        
            for key in solution_keys:
                # interpolators is a dictionary containing all the interpolation objects
                # specific interpolator object selected by [defect][key]
                # passing (input_set) performs the interpolation and returns a list of size 1 
                # indexing 0 selects the interpolated float value
                solutions[key] = interpolators[defect][key](input_set)[0]
        
            defect_solutions[defect] = solutions
        
        interpolated_results.append(defect_solutions)
        
    return interpolated_results

def create_interpolator_dictionary(geometry_defects, solution_keys):
    interpolators = {}
    
    for defect in geometry_defects:
        defect_interpolators = {}
    
        for idx, solution in enumerate(solution_keys):
            try:
                root_path = pathlib.Path(__file__).resolve().parent
                path = pathlib.PurePath.joinpath(root_path, 'solutions', defect, defect + '_' + solution + '_solutions.csv')
                defect_interpolators[solution] = create_interpolator_object(path)
            except Exception as e:
                print(defect, 'is not a valid geometry defect,', repr(e))
                sys.exit()
                
        interpolators[defect] = defect_interpolators
        
    return interpolators

def create_interpolator_object(csv):
    solutions = pd.read_csv(csv)

    ac = json.loads(os.environ.get('AC'))
    ah = json.loads(os.environ.get('AH'))
    hri = json.loads(os.environ.get('HRI'))
    points = (ac, ah, hri)
    solutions_df = []
    row_counter = 0

    # formats the csv into a list of lists
    for x in range(len(ac)):
        y_list = []
        
        for y in range(len(ah)):
            y_list.append(solutions.iloc[row_counter].values)
            row_counter += 1
        solutions_df.append(y_list)

    # see scipy.interpolate.regulargridinterpolator
    interpolator = rgi(points, solutions_df, method='linear', bounds_error=False, fill_value = np.nan)
    return interpolator
