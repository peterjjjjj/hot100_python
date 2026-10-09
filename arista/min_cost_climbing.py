#LC746
def minCostClimbingStairs(self, cost: list[int]) -> int:
    dp_table = [0 for _ in range(len(cost))]
    dp_table[0] = cost[0]
    dp_table[1] = cost[1]

    for i in range(2, len(cost)):
        dp_table[i] = min(dp_table[i - 1], dp_table[i - 2]) + cost[i]

    return min(dp_table[-1], dp_table[-2] )

