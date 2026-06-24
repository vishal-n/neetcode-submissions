class Solution:
    def countBits(self, n: int) -> List[int]:
        
        lst = []

        for i in range(n+1):

            curr_num = str(bin(i))
            lst.append(curr_num.count('1'))
        
        return lst
