class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []
        open_braces = ['(', '{', '[']
        brackets_map = {')': '(', '}': '{', ']': '['}

        for i in range(len(s)):

            if s[i] in open_braces:
                stack.append(s[i])
            
            if s[i] in brackets_map:
                if not stack or stack[-1] != brackets_map[s[i]]:
                    return False
                stack.pop()
        
        if stack:
            return False
        else:
            return True

