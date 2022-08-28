from xml.dom.expatbuilder import theDOMImplementation
import numpy as np



# def set_field(data):
#     for i in range(len(data)):
#         if data[i]:
#             fix_tile(i,data[i]) 


def print_field(field):
    print('+-------+-------+-------+')
    for big_y in range(0,9,3):
        for y in range(big_y,big_y+3):
            print(end = '| ')
            for big_x in range(0,9,3):
                for x in range(big_x,big_x+3):
                    i = y*9+x
                    if field[i] :
                        print(field[i],end = " ")
                    else:
                        print(end= '  ')
                print(end = '| ')
            print()
        print('+-------+-------+-------+')





# def find_next_tryout(field = field):
#     possibles = np.where(field ==0)[0]
#     possible_options = options[possibles]
#     argmin = possible_options.sum(1).argmin()
#     return possibles[argmin]

# def fix_tile(tile,value):
#     for i in range(9):
#         options[tile][i] = False
#     options[tile][value-1] = True
#     set_tile(tile,value)

#     def set_tile(tile,value):
#         # print(f"setting_tile {tile} {value}")
#         assert field[tile] == 0
#         field[tile] = value
#         history.append((set_tile,tile,value))
#         res = True
#         for related in relations[tile]:

#             if not remove_option(related,value):
#                 # traceback()
#                 res = False
#         return res 



# def tryout(field = field):
#     nexttry = find_next_tryout(field)
#     try:
#         new_value = np.where(options[nexttry])[0][0]
#     except:
#         traceback()

#     if not try_tile(nexttry,new_value+1):
#         traceback()

# def try_tile(field,value):
#     history.append((try_tile,field,value))
#     return set_tile(field,value)

# def revert(action):
#     action,tile,value = action
#     if action == remove_option:
#         options[tile][value] = True
#         field[tile] = 0
#     elif action == set_tile:
#         field[tile] = 0


# def traceback():
#     last_action = history.pop()
#     while last_action [0] != try_tile:
#         revert(last_action)
#         try:
#             last_action = history.pop()
#         except:
#             print("no solution possible")
#             raise ValueError
#     action, tile,value = last_action
#     # options[tile][value-1] = False
#     if not remove_option(tile,value):
#         traceback()

# def solve():
#     while (field == 0).sum()>0:
#         try:
#             tryout()
#         except:
#             break
#     print_field()

