class Solution:
    def jump(self, nums: List[int]) -> int:
        
        min_jumps = 0
        curr_end = 0
        farthest = 0

        for i in range(len(nums)-1):

            farthest = max(farthest, i+nums[i])

            if i == curr_end:
                min_jumps += 1
                curr_end = farthest
        
        return min_jumps
