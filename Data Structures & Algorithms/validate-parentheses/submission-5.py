class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []

        if len(s) % 2 != 0:
            return False

        for i in range(len(s)):

            if s[i] in '([{':
                stack.append(s[i])
            
            elif s[i] == ')':
                if '(' in stack:
                    stack.pop()
                else:
                    return False
                
            
            elif s[i] == '}':
                if '{' in stack:
                    stack.pop()
                else:
                    return False
            
            elif s[i] == ']':
                if '[' in stack:
                    stack.pop()
                else:
                    return False
        
        if stack:
            return False
        
        return True
