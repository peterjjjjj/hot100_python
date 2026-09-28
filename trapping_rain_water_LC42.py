from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:

        left, right = 0, len(height) - 1
        highest_left, highest_right = 0, 0
        water = 0

        while left < right:
            if height[left] > highest_left:
                highest_left = height[left]
            elif height[right] > highest_right:
                highest_right = height[right]

            curr_water = min(highest_left, highest_right) - height[left]
            water += curr_water

            if height[left] <= height[right]:
                left += 1
            else:
                right -=1

        return water


if __name__ == '__main__':
    test = Solution()
    print(
        test.trap(height = [0,1,0,2,1,0,1,3,2,1,2,1])
    )



        


