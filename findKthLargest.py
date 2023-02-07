import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        heap = []
        heapq.heapify(heap)
        
        for num in nums:
            heapq.heappush(heap , -num)
        result = None
        for i in range(k):
            result = heapq.heappop(heap)
        return -result
