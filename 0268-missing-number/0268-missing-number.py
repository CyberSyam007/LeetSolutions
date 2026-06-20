class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums=sorted(nums)
        l=len(nums)
        for i in range(l+1):
            if i not in nums:
                return i
                
        