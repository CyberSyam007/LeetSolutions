class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.

        """
        lol=[]
        counter=0
        for i in nums:
            if i==0:
                counter+=1
            else:
                lol.append(i)

        for i in range(len(nums)):
            if len(lol) > i:
                nums[i]=lol[i]
            else:
                nums[i]=0
        return nums


