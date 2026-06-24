class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        freq = [0] * 26
        left = 0
        max_count = 0
        max_len = 0

        for right in range(len(s)):

            freq[ord(s[right]) - ord('A')] += 1
            max_count = max(max_count, freq[ord(s[right]) - ord('A')])

            while (right - left + 1) - max_count > k:
                freq[ord(s[left]) - ord('A')] -= 1
                left += 1

            max_len = max(max_len, right-left+1)
        
        return max_len
