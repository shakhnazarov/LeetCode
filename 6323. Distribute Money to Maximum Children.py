class Solution:
    def distMoney(self, money: int, children: int) -> int:
        if children > money:
            return -1
        ans = 0
        while money > 0 and children > 0:
            money -= 8
            children -= 1
            if children > money:
                break
            ans += 1

        if money == -4 and children == 0:
            ans -= 1
        if money > 0 and children == 0:
            ans -= 1
        return ans

