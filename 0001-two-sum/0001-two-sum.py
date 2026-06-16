class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        s1=sorted(nums)
        i=0
        result=[]
        final=[]
        j=len(nums)-1
        while i<j and j>=0:
            temp=s1[i]+s1[j]
            if temp == target:
                result=[s1[i],s1[j]]
                break
            elif temp > target:
                j-=1
            else:
                i+=1
        
        if result!=[]:
        
            for i in range(len(nums)):
                if nums[i] in result:
                    final.append(i)
            return final
        else:
            return []


        