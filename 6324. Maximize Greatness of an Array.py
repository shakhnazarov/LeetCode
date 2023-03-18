class Solution:
    def maximizeGreatness(self, nums: List[int]) -> int:
        nums_d = collections.Counter(nums)

        # sort dict keys
        nums_d_s = sorted(nums_d)

        nums_d_i = {}
        for i, num in enumerate(nums_d_s):
            nums_d_i[num] = i

        nums_d_copy = nums_d.copy()
        l = 0
        r = 1
        ans = 0

        while r < len(nums_d_s):
            if l == r:
                r += 1
            if r == len(nums_d_s):
                break
            count_prev = nums_d[nums_d_s[l]]
            count_now = nums_d_copy[nums_d_s[r]]
            while count_prev > count_now:
                count_prev -= count_now
                ans += count_now
                r += 1
                if r == len(nums_d_s):
                    break
                count_now = nums_d_copy[nums_d_s[r]]

            if r != len(nums_d_s):
                ans += count_prev
                nums_d_copy[nums_d_s[r]] -= count_prev
            l += 1

        return ans