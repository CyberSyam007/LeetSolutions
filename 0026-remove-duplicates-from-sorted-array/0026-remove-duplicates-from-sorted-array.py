class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        s=sorted(set(nums))
        for i in range(len(s)):
            nums[i]=s[i]
        return(len(s))
