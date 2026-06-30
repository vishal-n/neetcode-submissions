class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        num_freq = {}

        for i in range(len(nums)):
            if nums[i] in num_freq:
                num_freq[nums[i]].append(i)
            else:
                num_freq[nums[i]] = [i]
        
        for i in range(len(nums)):
            if target-nums[i] in num_freq:
                if i != num_freq[target-nums[i]][0]:
                    return [i, num_freq[target-nums[i]][0]]
                else:
                    a = i
                    b = num_freq[target-nums[i]][0]
                    return [min(a, b), max(a, b)]
