class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        if len(nums) % k != 0:
            return False

        nums_sorted = sorted(nums)
        dict_sorted = {}
        for num in nums_sorted:
            dict_sorted[num] = 1 + dict_sorted.get(num, 0)

        marker = next(iter(dict_sorted))
        while True:
            for num in range(marker, marker + k):
                if dict_sorted.get(num, 0) == 0:
                    return False
                dict_sorted[num] -= 1
                if dict_sorted[num] == 0:
                    del dict_sorted[num]

            if len(dict_sorted) == 0:
                return True
            marker = next(iter(dict_sorted))