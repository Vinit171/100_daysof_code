class Solution:
    def firstUniqChar(self, s: str) -> int:
        lk = list(s)
        l = []
        lkk = []

        for m in lk:
            if m in l:
                lkk.append(m)

            else:
                l.append(m)
        t = set(lkk)
        mn = list(t)
        for nn in mn:
            l.remove(nn)

        if len(l) != 0:
            t = lk.index(l[0])
            return (t)
        else:
            return (-1)