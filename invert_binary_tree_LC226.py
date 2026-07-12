from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        TC: O(n)
        SC: O(1)
        :param root:
        :return:
        """

        if root is None:
            return root

        left = self.invertTree(root.left)
        right = self.invertTree(root.right)
        root.left, root.right = right, left
        return root


if __name__ == '__main__':
    test = TreeNode(2)
    test.left = TreeNode(1)
    test.right = TreeNode(3)
    result = (Solution().invertTree(test))
    print(result)

