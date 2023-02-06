# Tims SIF Interpolator
This module performs 3D interpolation for stress intensity factor coefficients, necessary to do calculations for fatigue crack growth analysis. To see the currently supported geometry defects, review the `.env` file (may be hidden) or the solutions subfolder.

This package was developed with the intention to integrate with a larger fatigue crack growth program.

## Usage Instructions
1. Read these instructions in their entirety before doing them.
2. Clone this repository from Github. 
3. Ensure all files and folders are located in the same directory as the fatigue crack growth program.
    * Research "importing modules from other directories" if you wish to organize the files.
4. Ensure the necessary packages and dependancies are installed, see `requirements.txt`.
    * It is recommended to run `tims_SIF_interpolator` from within a virtual environment.
    * You can install the necessary packages, within a virtual environment, ensuring your terminal is in the same working directory with `pip install -r requirements.txt`. 
        * Make sure your current working directory is in the same directory as `requirements.txt`.
5. See below example code on how to integrate the interpolator within the fatigue crack growth program, or run the script `example.py`.

```
import tims_SIF_interpolator

inputs = [[0.8, 0.8, 0.8], [0.5, 0.5, 0.5]]
geometry_defects = ['LDSE']

interpolated_results = tims_SIF_interpolator.interpolate(inputs, geometry_defects)

>>> interpolated_results
[{'LDSE': {'i0_depth': 1.0918, 'i0_surface': 1.09632, 'i1_depth': 0.63228, 'i1_surface': 0.22832, 'i2_depth': 0.47751999999999994, 'i2_surface': 0.094308, 'i3_depth': 0.39771999999999996, 'i3_surface': 0.051204}}, {'LDSE': {'i0_depth': 1.124, 'i0_surface': 0.911, 'i1_depth': 0.65, 'i1_surface': 0.1745, 'i2_depth': 0.4905, 'i2_surface': 0.0701, 'i3_depth': 0.4075, 'i3_surface': 0.037750000000000006}}]

>>> interpolated_results[0]
{'LDSE': {'i0_depth': 1.0918, 'i0_surface': 1.09632, 'i1_depth': 0.63228, 'i1_surface': 0.22832, 'i2_depth': 0.47751999999999994, 'i2_surface': 0.094308, 'i3_depth': 0.39771999999999996, 'i3_surface': 0.051204}}  

>>> interpolated_results[0]['LDSE']
{'i0_depth': 1.0918, 'i0_surface': 1.09632, 'i1_depth': 0.63228, 'i1_surface': 0.22832, 'i2_depth': 0.47751999999999994, 'i2_surface': 0.094308, 'i3_depth': 0.39771999999999996, 'i3_surface': 0.051204}

>>> interpolated_results[0]['LDSE']['i2_depth']
0.47751999999999994
```

## To do

* Replacing .env with ENUMS or global variables.
* Docstrings for functions and files.
* Error-handling for external module codes, e.g. SciPy Regular Grid Interpolator.
* General user error-handling.
* Optimise functions - one function, one responsibility.
* General Tim next-check.

***If nothing works, definitely do not see Timothy Cameron.***