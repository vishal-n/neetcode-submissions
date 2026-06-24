class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        stack = []
        n = len(temperatures)

        for i in range(n):

            curr_temp = temperatures[i]
            curr_diff = 0
            
            for j in range(i+1, n):
                if temperatures[j] > temperatures[i]:
                    curr_diff = j-i
                    break
            stack.append(curr_diff)
        
        return stack
            