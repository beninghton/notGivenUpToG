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

q = TreeNode(1)
t = q
#l = TreeNode(2)
#q.left = l
r = TreeNode(3)
q.right = r
q = q.right
r = TreeNode(4)
q.right = r
q = q.right
r = TreeNode(5)
q.right = r
q = t

class Solution:


    def mergeTrees(self, t1, t2):

        # Base Cases. Результат записываем в левое дерево, его и возвращаем.
        # Если оба пустые - возвращаем None.
        if not t1 and not t2:
            return None

        # Если оба есть - склдываем значения в первое дерево, ничего не возвращаем, идем дальше.
        elif t1 and t2:
            t1.val += t2.val

        # Если пустой один из них - возвращаем тот, что не пустой.
        # Соответственно все дети его так же копируются, но по ним мы не идем, т.к. возвращаем и пойдем уже вверх по стеку.
        elif t1 is None:
            return t2
        elif t2 is None:
            return t1

        # Левые пути проходим и возвращаем все в t1.left, затем правые возвращаем в t1.right и возвращаем t1.
        t1.left = self.mergeTrees(t1.left, t2.left)
        t1.right = self.mergeTrees(t1.right, t2.right)

        return t1


#Complexity Analysis
#Time complexity : O(m). A total of mm nodes need to be traversed. Here, m represents the minimum number of nodes from the two given trees.
#Space complexity : O(m). The depth of the recursion tree can go upto m in the case of a skewed tree. In average case, depth will be O(logm).

    def mergeTrees_iter(self, t1, t2):

        #Определяем очереди
        from collections import deque

        t1_queue = deque()
        t2_queue = deque()

        # Проверяем на пустоту входные деревья
        if not t1 and not t2:
            return None

        elif not t1 or not t2:
            return t1 or t2

        else:
            t1_head = t1
            t1_queue.appendleft(t1)
            t2_queue.appendleft(t2)

        # Пока очереди не пустые
        while t1_queue and t2_queue:
            # Снимаем с очереди
            t1 = t1_queue.pop()
            t2 = t2_queue.pop()

            # Сложили в t1 сумму
            t1.val += t2.val

            # Если есть оба левые, добавляем в очередь
            if t1.left and t2.left:
                t1_queue.appendleft(t1.left)
                t2_queue.appendleft(t2.left)
            # Если есть оба правые, добавляем в очередь
            if t1.right and t2.right:
                t1_queue.appendleft(t1.right)
                t2_queue.appendleft(t2.right)

            # Если t1 пустой, но есть t2 - пихаем все в t1, иначе ничего не делаем. Т.к. возвращать будем t1
            if t1.left is None and t2.left:
                t1.left = t2.left
            if t1.right is None and t2.right:
                t1.right = t2.right

        return t1_head

#Complexity Analysis
#Time complexity : O(n). We traverse over a total of n nodes. Here, n refers to the smaller of the number of nodes in the two trees.
#Space complexity : O(n). The depth of stack can grow upto n in case of a skewed tree.


def iter_tree(t):

    if t:
        print(t.val)
        iter_tree(t.left)
        iter_tree(t.right)
    else:
        return

sol = Solution()

#t3 = sol.mergeTrees(p, q)
t3 = sol.mergeTrees_iter(p, q)
iter_tree(t3)






