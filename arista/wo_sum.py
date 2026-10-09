class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen = {}

        for index, num in enumerate(nums):
            needed = target - num

            if needed in seen:
                return [seen[needed], index]

            seen[num] = index

        return []