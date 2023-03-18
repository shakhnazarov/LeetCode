"""
Don't need to know exact location of numbers, only the parity and quantity
"""

class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        counts = {}
        for num in nums:
            counts[num] = 1 + counts.get(num, 0)

        answer = [0, 0]
        for count in counts.values():
            if count % 2 == 1:
                answer[1] += 1

            answer[0] += count // 2

        return answer


