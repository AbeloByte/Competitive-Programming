class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        permutation_order = []
        for values in nums :
            permutation_order.append(nums[values])
        return permutation_order

        

        