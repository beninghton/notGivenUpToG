# -*- coding: utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


p = TreeNode(1)
l = TreeNode(2)
p.left = l
#r = TreeNode(3)
#p.right = r

q = TreeNode(1)
l = TreeNode(2)
q.left = l
root = q
q = q.left
r = TreeNode(3)
q.left = r


class Solution:
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """

        # Идем по всем нодам как DFS, когда доходим до конца - смотрим равен ли сумме. Если хоть 1 раз равен, возвращаем True и оно доходит вверх.
        def helper_dfs(node, count):
            if node is None:
                return False

            count += node.val

            if node.left is None and node.right is None:
                if count == sum:
                    return True
                else:
                    return False

            return helper_dfs(node.left, count) or helper_dfs(node.right, count)

        if root is None:
            return False

        return helper_dfs(root, 0)

# T - O(N) - count all nodes down to the leaf
# S - O(1)



sol = Solution()
print(sol.hasPathSum(root, 6))

# T - O(N) - nodes count
# S - O(1) - no additional space