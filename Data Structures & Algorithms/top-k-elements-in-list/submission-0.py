class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        freq_map = {}
        final_lst = []

        for num in nums:
            if num in freq_map:
                freq_map[num] += 1
            else:
                freq_map[num] = 1
        
        num_freq_lst = [(key, val) for key,val in freq_map.items()]
        sorted_freq_lst = sorted(num_freq_lst, key=lambda x: x[1])[::-1]

        for i in range(k):
            final_lst.append(sorted_freq_lst[i][0])
        
        return final_lst

        



