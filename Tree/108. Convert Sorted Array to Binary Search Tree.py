# -*- coding: utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None





class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        # Начинаем с середины, и дальше левые ноды у нас будут слева от середины, а правые с права, таким образом будет достигнута балансность.

        def helper(l, r):

            # Base case, если левый индекс превысил правый
            if l > r:
                return

            # Определяем середину, и берем ее значение как рутовую ноду. Ее и вернем.
            m = (l + r) // 2
            node = TreeNode(nums[m])

            # Дальше определяем left и right для рутовой ноды по рекурсии.
            node.left = helper(l, m - 1)
            node.right = helper(m + 1, r)
            return node

        node = helper(0, len(nums) - 1)
        return node


# O(N) - все ноды пройдем. O(1) - доп память кроме входного листа мы не используем.







sol = Solution()
res_node = sol.sortedArrayToBST([-10, -3, 0, 5, 9])


def iter_node_dst(node):
    if node is None:
        return
    print(node.val)
    iter_node_dst(node.left)
    iter_node_dst(node.right)


def iter_node_bst(node):
    from collections import deque
    q = deque()

    q.append(node)

    while q:
        node = q.popleft()
        if node is None:
            print(None)
        else:
            print(node.val)
            if node.left is None and node.right:
                q.append(node.left)
                q.append(node.right)
            elif node.left and node.right is None:
                q.append(node.left)
            elif node.left and node.right:
                q.append(node.left)
                q.append(node.right)


iter_node_bst(res_node)






