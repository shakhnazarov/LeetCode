import heapq


class Solution:
    def findScore(self, nums: List[int]) -> int:
        heap = []
        visited = [False for _ in range(len(nums))]
        for i, num in enumerate(nums):
            heapq.heappush(heap, (num, i))

        score = 0
        while heap:
            value, ind = heapq.heappop(heap)
            if not visited[ind]:
                score += value
                visited[ind] = True
                if ind > 0:
                    visited[ind - 1] = True
                if ind + 1 < len(nums):
                    visited[ind + 1] = True

        return score