class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        num_freq = {}

        for i in range(len(nums)):
            num_freq[nums[i]] = i
        
        for i in range(len(nums)):
            if target-nums[i] in num_freq:
                return [i, num_freq[target-nums[i]]]
        



