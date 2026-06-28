import heapq


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        lst = nums[:k]
        heapq.heapify(lst)

        for i in range(len(nums)):
            if lst[-1] > nums[i]:
                heapq.heappop(lst)
                heapq.heappush(lst, nums[i])
            else:
                heapq.heappush(lst, nums[i])
        
        return lst[-1]