class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)==0 or len(s)%2!=0:
            return False
        l=list(s)
        d={'()':0,'[]':0,'{}':0}
        i=0
        while True:
            if len(l)==0:
                return True
            if l[i]+l[i+1] in d:
                l.pop(i)
                l.pop(i)
                i=0
            else:
                i+=1
                if i==(len(l)-1):
                    return False



"""
class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)==0 or len(s)%2!=0:
            return False
        l=list(s)
        d={'(':')','[':']','{':'}',')':0,'}':0,']':0}
        #l=}}
        while True:
            i=0
            if len(l)==0:
                return True
            while True:
                if d[l[i]]==l[i+1]:
                    l.pop(i)
                    l.pop(i)
                    break
                else:
                    i+=1
                    if i==(len(l)-1):
                        return False
            
"""     