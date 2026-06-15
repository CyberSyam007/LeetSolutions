class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dic={}
        for i in range(len(nums)):
            if nums[i] not in dic:
                dic[nums[i]]=1
            else:
                dic[nums[i]]+=1
        size=len(nums)//2
        for i in dic:
            if dic[i] > size:
                return i

        