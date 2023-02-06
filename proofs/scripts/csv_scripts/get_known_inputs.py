from dotenv import load_dotenv
import json
import os

def get_known_inputs():
    load_dotenv()

    geometry_defects = json.loads(os.environ.get('KNOWN_GEOMETRIES'))
    ac_inputs = json.loads(os.environ.get('AC'))
    ah_inputs = json.loads(os.environ.get('AH'))
    hri_inputs = json.loads(os.environ.get('HRI'))
    inputs = []

    # required formating when passing arguments to the tims_SIF_interpolator.interpolate() function
    for ac in ac_inputs:
        for ah in ah_inputs:
            for hri in hri_inputs:
                inputs.append([ac, ah, hri])
    
    return inputs, geometry_defects
