class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        if amount == 0:
            return 0
        if not coins:
            return -1

        res = [1000000 for x in range(amount + 1) ]
        res[0] = 0

        for amt in range(1, amount + 1):
            for coin in coins:
                if coin <= amt:
                    res[amt] = min(res[amt], res[amt - coin] + 1)

        if res[amount] == 1000000:
            return -1
        else:
            return res[amount]

s = Solution()
r = s.coinChange([338,26,303,41,167,331,485,239,332],
8966)
print(r)