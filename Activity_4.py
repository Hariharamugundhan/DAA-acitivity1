# Climbing stairs
def climbStairs(n):
    if n <= 2:
        return n

    a, b = 1, 2
    for _ in range(3, n+1):
        a, b = b, a + b

    return b

# House robber
def rob(nums):
    prev, curr = 0, 0

    for num in nums:
        prev, curr = curr, max(curr, prev + num)

    return curr

# Coin change
def coinChange(coins, amount):
    dp = [float("inf")] * (amount + 1)
    dp[0] = 0

    for i in range(1, amount + 1):
        for coin in coins:
            if i - coin >= 0:
                dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[amount] if dp[amount] != float("inf") else -1

#  Longest common subsequence
def longestCommonSubsequence(text1, text2):
    dp = [[0]*(len(text2)+1) for _ in range(len(text1)+1)]

    for i in range(len(text1)-1, -1, -1):
        for j in range(len(text2)-1, -1, -1):
            if text1[i] == text2[j]:
                dp[i][j] = 1 + dp[i+1][j+1]
            else:
                dp[i][j] = max(dp[i+1][j], dp[i][j+1])

    return dp[0][0]

# Number of 1 bits
def hammingWeight(n):
    count = 0
    while n:
        count += n & 1
        n >>= 1
    return count
