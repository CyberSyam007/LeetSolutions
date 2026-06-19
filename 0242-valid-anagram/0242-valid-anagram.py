class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        def makeaset(s: str):
            d={}
            for i in s:
                if i not in d:
                    d[i]=1
                else:
                    d[i]+=1
            return d
        ss=makeaset(s)
        st=makeaset(t)
        if ss==st:
            return True
        else:
            return False