class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        result=[]
        nums=sorted(nums)
        for i in range(len(nums)):
            j=i+1
            k=len(nums)-1
            if i>0 and nums[i]==nums[i-1]:
                continue
            while j<k and k>=0:
                if nums[j]+nums[k]+nums[i]==0:
                    temp=[nums[i],nums[j],nums[k]]   
                    result.append(temp)
                    while j<k and nums[j]==nums[j+1]: j+=1
                    while j<k and nums[k-1]==nums[k]: k-=1
                    
                    j+=1
                    k-=1
                elif nums[j]+nums[k]+nums[i] >0:
                    k-=1
                else:
                    j+=1
        return result


        