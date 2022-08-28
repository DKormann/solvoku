import numpy as np


"""for each tile we have an array of the indices that are somehow connected to the tile and should not have the same number"""
relations = [[]for _ in range(81)]

for i in range(9):

    """indices of the 9 rows"""
    row_indices = [[x+y*9 for x in range(9)] for y in range(9)]

    for tile in row_indices[i]:
        for neighbour in row_indices[i]:
            if neighbour != tile and neighbour not in relations[tile]:
                relations[tile].append(neighbour)

    """indices of the 9 columns"""
    col_indices = [[x+y*9 for y in range(9)] for x in range(9)]

    for tile in col_indices[i]:
        for neighbour in col_indices[i]:
            if neighbour != tile and neighbour not in relations[tile]:
                relations[tile].append(neighbour)

    """indiced of the 9 boxes"""
    box_indices = []
    for X in range(0,9,3):
        for Y in range(0,9,3):
            box = [x+y*9 for y in range(X,X+3) for x in range(Y,Y+3)]
            box_indices.append(box)

    for tile in box_indices[i]:
        for neighbour in box_indices[i]:
            if neighbour != tile and neighbour not in relations[tile]:
                relations[tile].append(neighbour)

def remove_option(options,field,history,tile,value):
    """
    remove the option passed in value from the options for given tile
    and append the action to history if successfull
    return whether the remove option run without hitting some contradiction
    """
    # assert type(tile) == np.int64 or type(tile) == int, type(tile)
    # assert field.shape == (81,),field.shape

    success = True

    if field[tile] and  field[tile]== value: return False

    if field[tile]: return True

    value -= 1
    # check whether we can even remove the option 
    if options[tile][value]:
        options[tile][value] = False
        # if there is only one option left we want to fill 
        if options[tile].sum() == 1:
            new_value = np.where(options[tile])[0][0] +1
            set_tile(history,options,field,tile,new_value)

        history.append((remove_option,tile,value))
    return success

def revert(options,field,action):
    action,tile,value = action
    if action == remove_option:
        options[tile][value] = True
        field[tile] = 0
    elif action == set_tile:
        field[tile] = 0

def traceback(options,field,history):
    """go back in history to revert all chages up until last decision"""
    last_action = history.pop()
    while last_action [0] != try_tile:
        revert(options,field,last_action)
        try:
            last_action = history.pop()
        except:
            print("no solution possible")
            raise ValueError
    action, tile,value = last_action
    if not remove_option(options,field,history,tile,value):
        traceback(options,field,history)

def set_tile(history,options,field,tile,value):
    assert field[tile] == 0
    field[tile] = value
    history.append((set_tile,tile,value))
    res = True
    for related in relations[tile]:

        if not remove_option(options,field,history,related,value):
            res = False
    return res 

def try_tile(history,options,field,tile,value):
    """just calls set_tile and records in history"""
    history.append((try_tile,tile,value))
    return set_tile(history,options,field,tile,value)


def solve(field):

    options = np.array([[True]*9]*81)

    field = field.copy()
    # global options
    options = np.array([[True]*9]*81)
    history = []
    for i in range(81):
        if (val := field[i]):
            options[i] = np.array([False]*9)
            options[i][val-1] = True
            
            for neighbour in relations[i]:
                remove_option(options,field,history,neighbour,val)
    
    while (field == 0).any():

        possibles = np.where(field ==0)[0]
        possible_options = options[possibles]
        argmin = possible_options.sum(1).argmin()
        nexttry =  possibles[argmin]

        try:
            new_value = np.where(options[nexttry])[0][0]
        except: 
            traceback()

        if not try_tile(history,options,field,nexttry,new_value+1):
            traceback(options,field,history)
    return field

