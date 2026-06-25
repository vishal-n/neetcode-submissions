import heapq


class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.stream = nums
        self.k = k
        

    def add(self, val: int) -> int:
        self.stream.append(val)
        heapq.heapify(self.stream)
        return heapq.nlargest(len(self.stream), self.stream)[self.k-1]
        
