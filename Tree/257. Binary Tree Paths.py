# -*- coding: utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


"""
Input:

   1
 /   \
2     3
 \
  5

Output: ["1->2->5", "1->3"]

Explanation: All root-to-leaf paths are: 1->2->5, 1->3

input - [1], output [1]
input [1,2], output [1,2]


"""



class Solution:
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        # define vars
        ans = []
        s = ''

        # Base cases если ноды нет или она одна
        if root is None:
            return ans
        if root.left is None and root.right is None:
            ans.append(str(root.val))
            return ans

        # define helper
        def helper(s, node):
            # Base Case
            if node is None:
                return

            # Добавляем к ноде символ стрелочки.
            s += str(node.val) + '->'

            # Ок, если нет ни ливой ни правой ноды, добавляем в результат
            if node.right is None and node.left is None:
                # Убираем символ стрелочки и добавляем в лист как результат (минус 2 последних символа)
                ans.append(s[:len(s)-2])
            else:
                # Если правая еще есть, идем туда
                helper(s, node.right)
                helper(s, node.left)

        helper(s, root)
        # Возвращаем заполненый ансвер
        return ans

# T - O(N) - проходим все ноды
# S - O(N) - размер строки, а так же возвращаемого листа




sol = Solution()
res_node = sol.binaryTreePaths([-10, -3, 0, 5, 9])


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






