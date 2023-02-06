def iterate_through_inputs(inputs, index):
    list = []

    # inputs is a list of lists
    for subset in inputs:
        list.append(subset[index])
    
    return list
    