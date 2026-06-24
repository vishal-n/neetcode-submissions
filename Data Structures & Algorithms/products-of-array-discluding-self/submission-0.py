class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        prefix = 1
        suffix = 1
        final_arr = [1] * n

        for i in range(n):
            final_arr[i] *= prefix
            prefix *= nums[i]
        
        for i in range(n-1, -1, -1):
            final_arr[i] *= suffix
            suffix *= nums[i]
        
        return final_arr
