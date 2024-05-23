class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        w = 0 
        r = 0
        k = 0
        while r < len(nums):
            if nums[r]!=val:
                temp =nums[r]
                nums[r] = nums[w]
                nums[w]=temp
                w+=1
                k+=1
            r+=1
        return k
    
        