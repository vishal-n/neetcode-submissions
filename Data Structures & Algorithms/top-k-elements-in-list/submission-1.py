
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        freq_map = {}
        freq_lst = []

        for num in nums:
            if num in freq_map:
                freq_map[num] += 1
            else:
                freq_map[num] = 1
        
        for key, val in freq_map.items():
            freq_lst.append((key, val))
        
        lst = sorted(freq_lst, key=lambda x:x[1])[::-1][:k]

        return [item[0] for item in lst]

