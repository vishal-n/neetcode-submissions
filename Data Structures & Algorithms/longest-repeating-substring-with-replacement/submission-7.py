class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        if len(set(s)) == 1:
            return len(s)
        
        freq_map = {}
        stack = []
        highest_freq_char = ""
        count = k

        for char in s:
            if char in freq_map:
                freq_map[char] += 1
            else:
                freq_map[char] = 1
        
        freq_values = sorted(list(freq_map.values()))
        max_frequency = freq_values[-1]

        for char in freq_map:
            if freq_map[char] == max_frequency:
                highest_freq_char = char
                break
        
        for char in s:
            if char == highest_freq_char:
                stack.append(char)
            
            elif char != highest_freq_char and count > 0:
                stack.append(highest_freq_char)
                count -= 1
            else:
                break

        print("Stack: ", stack)
        
        return len(stack)






