class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = []
        for xx in matrix:
            l.extend(xx)

        if target in l:
            return (True)
        else:
            return (False)