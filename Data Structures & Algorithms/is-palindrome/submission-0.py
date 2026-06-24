class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        validated_str = [ch for ch in s if ch.isalnum()]
        return ''.join(validated_str).lower() == ''.join(validated_str).lower()[::-1]
