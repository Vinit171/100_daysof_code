class Solution:
    def isValid(self, s: str) -> bool:
        m = list(s)

        l=[]
        for qq in m:
            if len(l)==0:
                l.append(qq)
            elif (l[-1]=='{' and qq=='}') or (l[-1]=='[' and qq==']') or (l[-1]=='(' and qq==')'):
                #print(l,"dsfsf")
                l.pop()
            else:
                l.append(qq)

        #print(l)
        if len(l)==0:
            return True
        else:
            return False