import unittest
import numpy as np

class TestSum(unittest.TestCase):

    def test(self):
        from solver import solve

        data = np.array([
            0,0,9, 6,0,0, 1,0,0,
            0,1,0, 7,0,0, 0,8,0,
            3,5,0, 0,1,0, 0,0,0,
            
            5,0,0, 0,0,0, 6,0,0,
            0,0,0, 0,4,2, 0,0,1,
            0,0,3, 0,0,0, 0,7,0,

            0,0,5, 0,0,6, 0,1,0,
            0,0,6, 8,0,0, 3,0,4,
            0,8,1, 4,7,0, 2,0,0,
        ]) 
        solve(data)

if __name__ == "__main__":
    unittest.main()