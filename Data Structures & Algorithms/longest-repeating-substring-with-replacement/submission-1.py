class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        if len(s) == len(set(s)):
            return len(s)
        
        freq_map = {}

        for char in s:
            if char in freq_map:
                freq_map[char] += 1
            else:
                freq_map[char] = 1
        
        freq_values = sorted(list(freq_map.values()))

        if len(s) % 2 != 0:
            return freq_values[-1] - (freq_values[-1] - freq_values[-2]) + k + 1
        else:
            return freq_values[-1] - (freq_values[-1] - freq_values[-2]) + k
