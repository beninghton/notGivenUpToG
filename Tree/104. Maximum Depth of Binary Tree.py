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


class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # Global var to count depth
        max_depth = 0

        def helper(node, count):

            nonlocal max_depth
            # If we are None mean it's a leafe, write down counter, if it's bigger that current max_count.
            if node is None:
                if count > max_depth:
                    max_depth = count
                return

            # Go traverse through the tree
            count += 1
            helper(node.left, count)
            helper(node.right, count)


        helper(root, 0)
        return max_depth


sol = Solution()
print(sol.maxDepth(root))

# T - O(N) - nodes count
# S - O(1) - no additional space