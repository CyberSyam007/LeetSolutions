class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d={}
        for i in strs:
            temp=sorted(i)
            temp=''.join(temp)
            if temp not in d:
                d[temp]=[]
            
            d[temp].append(i)
        return list(d.values())



