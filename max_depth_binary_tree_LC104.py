from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        """
        Time Complexity: O(N)
        Space Complexity: O(1)
        :param root:
        :return:
        """

        if not root:
            return 0

        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)

        return 1 + max(left_depth, right_depth)


if __name__ == '__main__':
    test = TreeNode(3)
    test.left = TreeNode(9)
    test.right = TreeNode(20)
    test.right.left = TreeNode(15)
    test.right.right = TreeNode(7)
    print(Solution().maxDepth(test))




