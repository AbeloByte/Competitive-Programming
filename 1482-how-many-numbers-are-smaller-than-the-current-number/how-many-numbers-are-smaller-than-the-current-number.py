class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        # nums.sort()
        count = []
        for i in range(len(nums)):
            val = 0
            for j in range(0,len(nums)):
                if nums[i] > nums[j] and i !=j:
                   val+=1
            count.append(val)
        return count


        