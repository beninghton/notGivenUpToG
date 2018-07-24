# -*- coding: utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


p = TreeNode(1)
p_root = p
p1 = TreeNode(3)
p2 = TreeNode(2)
p3 = TreeNode(4)
p.left = p1
p = p.left
p.left = p2
p = p.left
p.left = p3



q = TreeNode(1)
l = TreeNode(2)
q.left = l
#r = TreeNode(3)
#q.right = r

class Solution:
    def inorderTraversal_recursive(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        # Base case
        if root is None:
            return []

        res = []

        # Define helper function
        def helper(node):

            # At first go to the left nodes until reach the end
            if node.left:
                helper(node.left)

            # When reach the end, add a node
            res.append(node.val)

            # Then go to the right if right node exists
            if node.right:
                helper(node.right)


        helper(root)
        return res

### Более короткое рекурсивное решение. Не проверяем на left и right. Сразу на root.
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        def dfs(root, result):
            if root:
                dfs(root.left,result)
                result.append(root.val)
                dfs(root.right,result)

        result = []

        dfs(root, result)

        return result


# Recursive solution.
# O(N), O(N)
# https://leetcode.com/problems/binary-tree-inorder-traversal/solution/


    # Iterative. Stack.
    def inorderTraversal_stack(self, root):

        # Base case
        if root is None:
            return []

        # Инициализируем стек, и лист для результата
        res = []
        stack = []
        stack.append(root)

        # Пока стек не пустой
        while stack:
            # Пока есть левые ноды, проматываем до конца, добавляя их в стек.
            while root.left:
                # Если еще не посещали ноду - добавляем в стек.
                if root.left.val != "visited":
                    root = root.left
                    stack.append(root)
                else:
                    break


            # Как только левые ноды закончились, начинаем доставать их из стека и добавлять в результирующий лист.
            root = stack.pop()
            res.append(root.val)

            # Помечаем их как "visited", чтобы не зайти в них по новой на цикле while root.left.
            root.val = "visited"

            # Дальше проверяем однократно, есть ли правая нода. Если да, добавляем ее в стек. И переключаемся на нее.
            if root.right:
                stack.append(root.right)
                root = root.right



        return res

# O(N), O(N)

    # Iterative. Stack. Optimal
    def inorderTraversal_stack_optimal(self, root):

        # Инициализируем стек, и лист для результата
        res = []
        stack = []
        curr = root

        # Пока стек не пустой или нода существует
        while curr or stack:
            # Пока нода есть, проходим влево до конца, добавляя в стек.
            while curr:
                stack.append(curr)
                curr = curr.left

            # Как только левые ноды кончились, забираем со стека верхнюю, добавляем ее в результат.
            # И Перемещаемся на правую ноду. И повторяем цикл.
            curr = stack.pop()
            res.append(curr.val)
            curr = curr.right

        return res











sol = Solution()

print(sol.inorderTraversal_stack_optimal(p_root))



