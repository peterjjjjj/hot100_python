class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        nums.sort()
        result = 0
        for num in nums:
            result ^= num

        return result