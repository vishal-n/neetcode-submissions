class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        subsets = []
        n = len(nums)

        for i in range(2 ** n):

            curr_bin_num = bin(i)[2:]
            curr_subset = []

            if len(curr_bin_num) < n:
                curr_bin_num = '0'* (n - len(curr_bin_num)) + curr_bin_num

            for i in range(len(curr_bin_num)):
                if curr_bin_num[i] == '1':
                    curr_subset.append(nums[i])
            
            subsets.append(curr_subset)

        return subsets




