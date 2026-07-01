class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        SC = O(1)
        TC = O(n^2)
        """

        nums.sort()

        outputs = []

        for i in range(len(nums)-2):
            small_index = i+1
            big_index = len(nums)-1

            #After the first round, check for duplicate number.
            if i > 0 and nums[i] == nums[i-1]:
                continue

            while small_index < big_index:
                if nums[i] + nums[small_index] + nums[big_index] == 0:
                    outputs.append([nums[i], nums[small_index], nums[big_index]])
                    small_index += 1
                    big_index -= 1

                    #Check duplicates for small and big.
                    while small_index < big_index and nums[small_index] == nums[small_index - 1]:
                        small_index += 1

                    while small_index < big_index and nums[big_index] == nums[big_index + 1]:
                        big_index -= 1


                elif nums[i] + nums[small_index] + nums[big_index] < 0:
                    small_index += 1
                elif nums[i] + nums[small_index] + nums[big_index] > 0:
                    big_index -= 1


        return outputs


if __name__ == '__main__':
    test = Solution()
    print(test.threeSum([-1,0,1,2,-1,-4]))

