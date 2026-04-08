class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if not amount:
            return amount

        memo = {}
        for coin in coins:
            memo[coin]=1

        def dp(val):
            if val in memo.keys():
                return memo[val]

            possibilities = [dp(val-coin) for coin in coins if val-coin >=0]
            if possibilities:
                memo[val]=1 + min(possibilities)
            else:
                memo[val]= math.inf
            return memo[val]

        result = dp(amount) 
        return result if result != math.inf else -1
        