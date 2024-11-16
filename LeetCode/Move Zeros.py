class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = 0
        r = 0

        # w = 0
        # while r < len(nums):
        #     if nums[r] !=0:
        #         temp = nums[r]
        #         nums[r] = nums[w]
        #         nums[w] = temp

        #         w +=1
        #     r+=1

        # return nums 

        # optimized
        while l < len(nums):
            if nums[l] != 0 :
                nums[l],nums[r] = nums[r],nums[l] 
                r+=1
            l+=1

        return nums
