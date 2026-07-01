class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        SC = o1
        TC = on
        """
        left, right = 0, len(height) - 1

        max_water = min(height[left], height[right]) * (right - left)

        while left < right:
            curr_water = min(height[left], height[right]) * (right - left)

            if curr_water > max_water:
                max_water = curr_water


            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_water

if __name__ == '__main__':
    solution = Solution()
    print(solution.maxArea([1,8,6,2,5,4,8,3,7]))
