class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []
        open_brackets = ['(', '[', '{']
        brackets_map = {')': '(', ']': '[', '}': '{'}

        for i in range(len(s)):

            if s[i] in open_brackets:
                stack.append(s[i])
            
            elif s[i] in brackets_map:
                if not stack or stack[-1] != brackets_map[s[i]]:
                    return False
                stack.pop()
        
        if not stack:
            return True
        
        return False



