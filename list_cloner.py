#clones list so it can't be passed by reference
def clone(input_list):
    result_list=[]
    for row in input_list:
        result_list.append([tile for tile in row])
    return result_list