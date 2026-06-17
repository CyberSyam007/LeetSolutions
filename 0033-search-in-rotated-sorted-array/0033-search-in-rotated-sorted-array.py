class Solution:
    def search(self, nums: List[int], target: int) -> int:
        for i,char in enumerate(nums):
            if char == target:
                return i
        return -1

        