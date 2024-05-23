class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        w = 0
        r = 0
        while r < len(nums):
            if nums[r] !=0:
                temp =nums[r]
                nums[r]=nums[w]
                nums[w] = temp
                w+=1
            r+=1

        