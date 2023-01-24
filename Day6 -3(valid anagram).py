class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        k = list(s)
        l = list(t)

        k.sort()
        l.sort()

        if k==l:
            return(True)
        else:
            return(False)