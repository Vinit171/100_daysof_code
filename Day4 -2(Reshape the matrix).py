import numpy as np

class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        l=[]
        for k in mat:
            for s in k:
                l.append(s)
        if len(l)!=(r*c):
            return(mat)
        else:
            arr = np.array(mat)
            qt = arr.reshape(r,c)
            l = qt.tolist()
            return(l)