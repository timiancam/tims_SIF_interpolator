from csv_scripts.iterate_through_inputs import iterate_through_inputs

def get_input_data(inputs, key):

    if key == 'ac':
        return iterate_through_inputs(inputs, 0)
    elif key == 'ah':
        return iterate_through_inputs(inputs, 1)
    elif key == 'hri':
        return iterate_through_inputs(inputs, 2)
        