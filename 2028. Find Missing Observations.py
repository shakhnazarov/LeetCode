"""
each time check whether constraints for plausible values of rolled dices are violated,
otherwise fill with standard values
"""
class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        sum_m = sum(rolls)
        sum_n = mean * (n + len(rolls)) - sum_m

        if sum_n < n or sum_n > 6 * n:
            return []

        ans = []
        temp_num = 6
        temp_sum = sum_n
        temp_n = n
        while temp_n:
            if temp_sum - temp_num < temp_n - 1:
                temp_num -= 1
            else:
                ans.append(temp_num)
                temp_sum -= temp_num
                temp_n -= 1

        return ans