# Proofs

The files in this folder detail how to retrieve the appropriate .csv files related to the 3D SIF interpolation. Please refer to the presentation for the validation of the 'tims_sif_interpolator' script.

## Excel Instructions

1. Read these instructions in their entirety before doing them.
2. Open the `Excel` subfolder retrieve the two .vb scripts.
3. Navigate to X:\Projects\EdF Energy\PRJ0002783\21 Analysis\010_SG_FEA\09_proc\03_FCG
4. Retrieve the file `PRJ0002783_21_010_B_09proc_03FCG_G.xlsm`.
5. Open the Excel File.
6. Make sure to enable macros.
7. Navigate to the `FCG` tab, found near the bottom of the excel window.
5. Navigate to the `Developer` tab found near the top of the excel window.
    * The `Developer` tab may be hidden.
    * If so, follow the instructions here: <https://support.microsoft.com/en-gb/office/show-the-developer-tab-e1192344-5e56-4d45-931b-e5fd9bea2d45>
6. Click the `Visual Basic` button. 
7. Copy the .vb scripts into the space with the other scripts.
7. Select the `generate_known_excel_results` and press the `Run` triangle.
8. Select the `generate_unknown_excel_results` and press the `Run` triangle. 
    * The spreadsheet and the code are fiddly, it is recommended to not do anything else with the PC whilst the scripts are running. (Don't even look at it funny!)
    * Otherwise the scripts won't run properly and you will get incorrect results.
    * The `generate_known_excel_results` script takes 10 minutes to run on an Assystem S&A laptop.
    * The `generate_unknown_excel_results` script takes 30 minutes to run on an Assystem S&A laptop.
9. The results are copied from the `known_results` and `unknown_results` tabs (found at the bottom of the excel window) into the .csv files in the parent directory.


## Python Instructions

1. Read these instructions in their entirety before doing them.
2. Make sure you have the appropriate packages installed.
    * See the `readme.md` in `tims_sif_interpolator`.
3. It is recommended to run the following scripts in a virtual environment. 
    * Make sure the packages in step 2 are installed in the virtual environment.
4. Run the `python_known_results_generator` script.
5. Run the `python_unknown_results_generator` script.
6. Run the `difference_check_known_results` script.
7. Run the `difference_check_unknown_results` script.
8. The results are already written to .csv files in the parent directory.

***If nothing works, definitely do not see Timothy Cameron.***