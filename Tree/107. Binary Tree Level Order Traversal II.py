# -*- coding: utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

p = TreeNode(1)
l = TreeNode(2)
p.left = l
r = TreeNode(3)
p.right = r
p.left.left = TreeNode(4)
r.left = TreeNode(5)
r.right = TreeNode(6)

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """

        # Берем defaultdict, с дефолтным значением листа. Будем добавлять в него:
        # ключ - уровень дерева, значение - лист, содержащий все значения нод на этом уровне.

        from collections import defaultdict
        res = []
        d = defaultdict(list)

        # Helper будет добавлять в словарь значения
        def helper(node, level):
            if node is None:
                return

            # Добавляем значение в зависимости от уровня. Для левых и правых уровень соответственно повышаем.
            d[level].append(node.val)
            node.left = helper(node.left, level + 1)
            node.right = helper(node.right, level + 1)


        helper(root, 0)

        # Добавляем в лист значения, реверсируем и возвращаем.
        for val in d.values():
            res.append(val)

        return res[::-1]


# O(N) - проходим все ноды. O(N) - для хранения нод в словаре и потом еще в результирующем листе.


    # Тут смысл такой, что просто идут через стек. И дальше пока стек не опустеет добавляют во временный лист значения.
    # Как только стек опустеет, значения добавляются в результирующий лист. Не оптимальное решение. Просто альтернатива.
    def levelOrderBottom_Leetcode(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        results = []
        if not root:
            return results
        queue = []
        # Сначала добавляем первую ноду в стек
        queue.append(root)
        while queue:
            # Пока стек есть, берем его длину
            count = len(queue)
            level = []
            # И собственно, пока все элементы не кончатся забираем их.
            while count != 0:
                # Level это временный лист.
                temp = queue.pop()
                level.append(temp.val)
                # Для каждой ноды добавляем ее левое и правое значение если есть.
                if temp.left:
                    # Вставляем на 0 значение. Сложность тут хуевая. O(N^2) получится из за insert (или что то такое, сложно оценить).
                    queue.insert(0, temp.left)
                if temp.right:
                    queue.insert(0, temp.right)
                count -= 1
            results.append(level)
        return results[::-1]


sol = Solution()
print(sol.levelOrderBottom(p))


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







