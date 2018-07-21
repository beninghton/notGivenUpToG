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
l = TreeNode(2)
q.left = l
#r = TreeNode(3)
#q.right = r

class Solution:
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        # Base case if root is empty
        if root is None:
            return True

        # If not, define recursive call and call it
        def recurs(root_l, root_r):

            # Чтобы определ зеркальное дерево или нет, идем одновременно по левой и правой стороне. И проверяем, равны ли значения. Если равны - идем дальше, пока не достигнем None.
            # Если достигли None одновременно, значит возвращаем True (ветки равны). И так проверяем сначала внешние ветки, затем внутренние.

            # Если обе ветки есть, значит можно проверить на равенство.
            if root_l and root_r:
                # Если равны - продолжаем вызывать стек, передавая ноды зеркально
                if root_l.val == root_r.val:
                    return recurs(root_l.left, root_r.right) and recurs(root_l.right, root_r.left)
                else:
                    return False
            # Если одной из них нет - значит 100% не зеркальное.
            elif root_l or root_r:
                return False
            # Третий случай, когда нет обоих - значит достигли дна одновременно. Возвращаем True.
            else:
                return True


        return(recurs(root.left, root.right))


#Complexity Analysis
#Time complexity : O(n). Because we traverse the entire input tree once, the total run time is O(n), where n is the total number of nodes in the tree.
# Не 2^n, потому что мы траверсим готовое дерево, а не решаем варианты и не производим по две ветки. Просто обходим все ноды 1 раз.
#Space complexity : The number of recursive calls is bound by the height of the tree. In the worst case, the tree is linear and the height is in O(n). Therefore, space complexity due to recursive calls on the stack is O(n) in the worst case.



    def isSymmetricIter(self, root):

        from collections import deque

        # Base cases
        if root is None:
            return True

        # Left for left nodes, right for right
        q_left = deque()
        q_right = deque()

        # If both exists - append them to the queues
        if root.left and root.right:
            q_left.append(root.left)
            q_right.append(root.right)
        # If one of them - it means that tree is not symmetric
        elif root.left or root.right:
            return False
        # If both does not exists = both None and it's True
        else:
            return True


        # Go in Loop

        while q_left and q_right:

            #Deque
            node_left = q_left.popleft()
            node_right = q_right.popleft()

            # Compare them, if not equal then False
            if node_left.val != node_right.val:
                return False

            # Then go lookup for rights and lefts of each of them
            # If both exist - add them to the queue.
            if node_left.left and node_right.right:
                q_left.append(node_left.left)
                q_right.append(node_right.right)
            # If not - return False. The tree is no symmetric
            elif node_left.left or node_right.right:
                return False

            # The same for the right ones
            if node_left.right and node_right.left:
                q_left.append(node_left.right)
                q_right.append(node_right.left)

            elif node_left.right or node_right.left:
                return False


        # If went out of sycle, it means that all values are equal and the queues is empty - we visited the all nodes. So return True.
        return True




#Complexity Analysis
#Time complexity : O(n). Because we traverse the entire input tree once, the total run time is O(n), where nn is the total number of nodes in the tree.
#Space complexity : There is additional space required for the search queue. In the worst case, we have to insert O(n) nodes in the queue. Therefore, space complexity is O(n)O(n).






























        # Define queues



sol = Solution()
print(sol.isSymmetric(p))