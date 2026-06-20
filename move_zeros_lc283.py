#LC 283, Move Zeroes

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        time complexity: O(n)
        space complexity: O(1)
        """

        if not nums or len(nums) == 1:
            return

        slow = 0

        for fast in range(len(nums)):
            if nums[fast] != 0:
                nums[slow], nums[fast] = nums[fast], nums[slow]

                slow += 1

        for i in range(slow, len(nums)):
            nums[i] = 0
