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
#q.left = r


class Solution:
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        # Если дошли до конца, надо вернуть True, иначе конечное выражение вернет None.
        if root is None:
            return True

        # Для каждой ноды смотрим ее left и right count.
        left = self.depth(root.left)
        right = self.depth(root.right)

        # Комплексное булево выражение.
        # Сначала смотрим больше ли разница между левой и правой. Дальше если устраивает, смотрим это для каждой левой ноды и правой ноды.
        return abs(left - right) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right)


    def depth(self, node):
        # Если конечная, возвращаем 0
        if node is None:
            return 0
        # Иначе возвращаем максимальный каунт с левой и правой ноды
        return max(self.depth(node.left), self.depth(node.right)) + 1



sol = Solution()
print(sol.isBalanced(root))


# For the current node root, calling depth() for its left and right children actually has to access all of its children, thus the complexity is O(N).
# We do this for each node in the tree, so the overall complexity of isBalanced will be O(N^2). This is a top down approach.

# S - O(1)

class Solution:
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.dfsHeight(root) != -1

    def dfsHeight(self, node):

        # If left and right nodes differ more than 1, we just return -1 = it's kind of False.
        if node is None:
            return 0

        left_height = self.dfsHeight(node.left)
        if left_height == -1:
            return -1

        right_height = self.dfsHeight(node.right)
        if right_height == -1:
            return -1

        if abs(left_height - right_height) > 1:
            return -1

        return max(left_height, right_height) + 1




sol = Solution()
print(sol.isBalanced(root))

#The second method is based on DFS. Instead of calling depth() explicitly for each child node, we return the height of the current node in DFS recursion.
#  When the sub tree of the current node (inclusive) is balanced, the function dfsHeight() returns a non-negative value as the height.
# Otherwise -1 is returned.
# According to the leftHeight and rightHeight of the two children, the parent node could check if the sub tree is balanced, and decides its return value.
# In this bottom up approach, each node in the tree only need to be accessed once. Thus the time complexity is O(N), better than the first solution.

# S - O(1)


# Такое же решение как и выше, но просто меняем переменную класса. И в конце ее возвращаем.
class Solution:

    result = True

    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        self.dfsHeight(root)
        return self.result

    def dfsHeight(self, node):

        # If left and right nodes differ more than 1, we just return -1 = it's kind of False.
        if node is None:
            return 0

        left_height = self.dfsHeight(node.left)

        right_height = self.dfsHeight(node.right)

        if abs(left_height - right_height) > 1:
            self.result = False

        return max(left_height, right_height) + 1