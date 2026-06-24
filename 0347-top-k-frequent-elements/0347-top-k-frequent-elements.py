class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d={}
        for i in nums:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        
        sorted_dict=dict((sorted(d.items(),key=lambda item:item[1], reverse=True)))
        result=[]
        c=0
        for i in sorted_dict:
            if c<k:
                result.append(i)
                c+=1
            else:
                break
        return result


