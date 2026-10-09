class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n

        dp_table = [0 for _ in range(n + 1) ]
        dp_table[1] = 1
        dp_table[2] = 2

        for i in range(3, n + 1):
            dp_table[i] = dp_table[i - 1] + dp_table[i - 2]

        return dp_table[n]
