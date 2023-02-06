import sys
import os
from csv_scripts.get_known_inputs import get_known_inputs
from csv_scripts.create_csv import create_csv 

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(os.path.dirname(current))
sys.path.append(parent)

# code above required to import below module in parent directory
import tims_SIF_interpolator

def main():
    inputs, geometry_defects = get_known_inputs()

    interpolated_results = tims_SIF_interpolator.interpolate(inputs, geometry_defects)

    create_csv(inputs, interpolated_results, 'python_known_results.csv')

main()
