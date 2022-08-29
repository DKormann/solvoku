from multiprocessing.util import sub_debug
from turtle import back
from xml.dom.expatbuilder import theDOMImplementation
import numpy as np

from solver import solve as backend_solve


def solve(sudoku):
    """pass soduko as string list or array"""
    data = []
    if type(sudoku) == str:
        for char in sudoku:
            try:
                next_int = int(char)
                data.append(next_int)
            except:
                pass
        assert len(data) == 81, 'cannot read data. sudoku needs to be 9x9'
        data = np.array(data)
    elif type(sudoku) == list:

        data = np.array(sudoku)

    elif type(sudoku) == np.ndarray:
        data = sudoku.flatten()
    else:
        raise ValueError("cannot interpret given data. data needs to be list array or string")

    result = backend_solve(data)
    print_field(result)




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

if __name__ == "__main__":
    intake = input("input sudoku data ")
    solve(intake)
