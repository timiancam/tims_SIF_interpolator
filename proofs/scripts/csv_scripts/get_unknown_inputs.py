from dotenv import load_dotenv
import json
import os
import numpy as np

def get_unknown_inputs():
    load_dotenv()

    geometry_defects = json.loads(os.environ.get('KNOWN_GEOMETRIES'))
    ac_inputs = np.arange(0.0,1.05,0.05)
    ah_inputs = np.arange(0.0,0.85,0.05)
    hri_inputs = np.arange(0.0,1.05,0.05)
    inputs = []

    # required formating when passing arguments to the tims_SIF_interpolator.interpolate() function
    for ac in ac_inputs:
        for ah in ah_inputs:
            for hri in hri_inputs:
                inputs.append([ac, ah, hri])
    
    return inputs, geometry_defects
