#LC 1, two sum

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        Time Complexity: O(n)
        Space Complexity: O(n)
        """

        if not nums or len(nums) < 2:
            return []

        #Hashmap for O1 space complexity.
        num_map = {}

        for i in range(len(nums)):
            remaining = target - nums[i]

            if remaining in num_map:
                return [num_map[remaining], i]

            num_map[nums[i]] = i

        return []