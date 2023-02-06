def get_coefficient_data(interpolated_results, variable_type):
    defect, solution = variable_type.split('_', 1)
    list = []

    for dictionary in interpolated_results:
        list.append(dictionary[defect][solution])

    return list
