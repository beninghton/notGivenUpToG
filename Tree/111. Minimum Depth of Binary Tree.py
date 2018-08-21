from collections import deque

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
#q = q.left
r = TreeNode(3)
q.right = r


class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0

        # Global var to count depth, initially it's maximum value
        min_depth = float('inf')

        def helper(node, count):

            nonlocal min_depth

            if node is None:
                return

            # Если мы идем по дереву и уже видим что count больше, тогда дальше нет смысла идти, возвращаемся сразу.
            if count > min_depth:
                return

            # If there is no left and no right, means it's a leaf. Compare counters and update.
            if node.left is None and node.right is None:
                if count < min_depth:
                    min_depth = count

            # Go traverse through the tree
            count += 1
            helper(node.left, count)
            helper(node.right, count)


        helper(root, 1)
        return min_depth

# T - O(min(N)) - nodes count. В худшем случае если левая ветка дерева равна правой полностью, т.е. дерево симметрично,
# худший случай будет O(N) - придется пройти все ноды.
# S - O(1) - no additional space

    # Interesting short solution
    def minDepth2(self, root):

        if root is None:
            return 0

        # Идем до конца дерева
        left = self.minDepth2(root.left)
        right = self.minDepth2(root.right)

        # Доходим до конца левой или правой стороны, и мы их складываем и прибавляем единицу.
        if left == 0 or right == 0:
            return left + right + 1
        # Если мы не в конце ноды, а получается выше, то находим минимальный путь.
        else:
            return min(left, right) + 1


    # Iterative solution
    def minDepth3(self, root):

        q = deque()
        level = 0

        if root is None:
            return 0
        else:
            q.append((root, level))

        # Пока очередь не пуста
        while q:
            # Достаем ноду и лвл
            node, level = q.popleft()

            # Если у ноды нет левых и правых нод, значит она - leaf. Мы дошли до минимума, прибавляем lvl и возвращаем его.
            if node.left is None and node.right is None:
                level += 1
                break

            # Пока есть левая или правая, значит нода не конечная, и мы добавляем ноды по очереди. Как BFS.
            # В итоге до конца дойдем, ничего не пропустив.
            if node.left:
                q.append((node.left, level + 1))

            if node.right:
                q.append((node.right, level +1))

        return level






sol = Solution()
print(sol.minDepth3(root))




