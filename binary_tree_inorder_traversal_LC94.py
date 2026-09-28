class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> list[int]:
        """
        Time Complexity: O(N)
        Space Complexity: O(1)
        :param root:
        :return:
        """

        output = []

        def dfs(node: TreeNode) -> None:
            if node is None:
                return

            dfs(node.left)
            output.append(node.val)
            dfs(node.right)

        dfs(root)
        return output


if __name__ == '__main__':
    testcase = TreeNode(1)
    testcase.left = TreeNode(0)
    testcase.right = TreeNode(2)
    testcase.right.left = TreeNode(3)

    print(Solution().inorderTraversal(testcase))
