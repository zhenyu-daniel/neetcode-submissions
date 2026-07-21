import numpy as np
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        arr = np.array(matrix)
        arr = np.flip(arr.T, axis=1)

        matrix[:] = arr.tolist()   # modify original list in place
    
        return 