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
#r = TreeNode(3)
#q.right = r

class Solution:
    def traverse(self, p):

        if not p:
            return

        print(p.val)
        self.traverse(p.left)
        self.traverse(p.right)

    def isSameTree(self, p, q):

        if p is None and q is None:     # It's Finish, it means that they both does not exist simultaneously, so they're equal
            return True

        elif not p or not q:                    # One of them exist but another does not. Return False
            return False

        else:                           # both exist, it means we do not finish yet
            if p.val == q.val:
                return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)    # Trying both simultaneously, either one of them
                                                                                                # fails or they both will end simultaneously
            else:
                return False




    def isSameTree_Iterative(self, a, b):

        # Если оба рута дерева пустые, как бы равны, True
        if not a and not b:
            return True
        # Или если один из них пустой, значит False
        elif not a or not b:
            return False

        from collections import deque
        queue_a = deque()
        queue_b = deque()

        # Добавляем руты деревьев в очередь
        queue_a.appendleft(a)
        queue_b.appendleft(b)

        # Пока очереди не пустые
        while queue_a and queue_b:

            # Забираем из очереди ноды
            a = queue_a.pop()
            b = queue_b.pop()

            if a.val != b.val:
                return False

            # Засовываем в очередь левые если оба(!) есть. Если оба пустые(!), в очередь просто не добавляем
            if a.left is not None and b.left is not None:
                queue_a.appendleft(a.left)
                queue_b.appendleft(b.left)
            elif a.left or b.left:
                # Если попал сюда, значит либо left либо right пустой - значит разные, сразу False.
                return False

            # Засовываем в очередь правые если оба есть. Если оба пустые(!), в очередь просто не добавляем
            if a.right is not None and b.right is not None:
                queue_a.appendleft(a.right)
                queue_b.appendleft(b.right)
            elif a.right or b.right:
                # Если попал сюда, значит либо left либо right пустой - значит разные, сразу False.
                return False

        # Если из while вышел, значит False не было и очередь закончилась - значит равны
        return True







sol = Solution()
#sol.traverse(p)
#print(sol.isSameTree(p, q))
print(sol.isSameTree_Iterative(p, q))



#Time Complexity:
# Complexity of the identicalTree() will be according to the tree with lesser number of nodes.
#  Let number of nodes in two trees be m and n then complexity of sameTree() is O(m) where m < n.