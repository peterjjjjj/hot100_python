#Easy prob but make sure to review

from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if not nums:
            return 0

        max_count = 0
        num_set = set(nums)

        for num in nums:
            #Check if this is the start of a sequence
            if (num-1) not in num_set:
                count = 1

                #Iterate for consecutive count
                while (num+1) in num_set:
                    count += 1
                    num += 1

                max_count = max(max_count, count)

        return max_count


if __name__ == '__main__':
    test = Solution()
    print(test.longestConsecutive(
        []
    ))