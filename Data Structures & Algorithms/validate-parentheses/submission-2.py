class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []

        if len(stack) % 2 != 0:
            return False

        for i in range(len(s)):

            if s[i] in '([{':
                stack.append(s[i])
            
            elif s[i] == ')' and '(' in stack:
                    stack.pop()
                
            
            elif s[i] == '}' and '{' in stack:
                stack.pop()
            
            elif s[i] == ']' and '[' in stack:
                stack.pop()
        
        if stack:
            return False
        
        return True
