class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)

        ans_set = {}
        for i, num in enumerate(nums):
            if target - num in ans_set:
                return [ans_set[target - num], i]
            else:
                ans_set[num] = i