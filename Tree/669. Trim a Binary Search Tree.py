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
l = TreeNode(2)
q.left = l
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
    def trimBST(self, root, L, R):

        return self.trim_bst_sub(root, L, R)

    def trim_bst_sub(self, node, L, R):

        # base case, current node is None, just Return
        if node is None:
            return

        # next, if val is more, go left, if less - go right, BECAUSE it's a binary tree
        if node.val < L:
            return self.trim_bst_sub(node.right, L, R)
        if node.val > R:
            return self.trim_bst_sub(node.left, L, R)

        # If node is in range, we found root. It's good. Then we need recursion it again to find left and right from the root
        else:
            node.left = self.trim_bst_sub(node.left, L, R)
            node.right = self.trim_bst_sub(node.right, L, R)

            # Return node(ROOT) at the end, with left and right already defined
            return node


#Complexity Analysis
#Time Complexity: O(N), where N is the total number of nodes in the given tree. We visit each node at most once.
#Space Complexity: O(N). Even though we don't explicitly use any additional memory, the call stack of our recursion could be as large as the number of nodes in the worst case.


    def trim_iter(self, root, L, R):

        # Сначала находим рута
        def get_root(root):

            while root is not None or root.val < L or root.val > R:
                if root.val < L:
                    root = root.right
                elif root.val > R:
                    root = root.left
                else:
                    return root

            return root


        # После того как новый рут найден, скармливаем его в новую функцию. Обрабатываем левую часть рута.
        # Если значение left меньше левой границы, его убираем, смотрим на правое, и т.д. Т.е. Либо/либо.
        # Пока не None, если левое значение так же не None, смотрим его значение. Если оно меньше левой границы - дальше в left идти не стоит, там будут значения еще меньше.
        # Значит присваеваем левому - правое значение. И т.д. Если значение в пределе, идем дальше влево.

        def trim_left(root):
            while root is not None:
                while root.left is not None and root.left.val < L:
                    root.left = root.left.right
                root = root.left

        # Аналогично поступаем с правой веткой.
        def trim_right(root):
            while root is not None:
                while root.right is not None and root.right.val > R:
                    root.right = root.right.left
                root = root.right


        # Прогоняем левую и правую с новым рутом и возвращаем.
        new_root = get_root(root)
        trim_left(new_root)
        trim_right(new_root)
        return new_root






def iter_tree(t):

    if t:
        print(t.val)
        iter_tree(t.left)
        iter_tree(t.right)
    else:
        return

sol = Solution()

#t3 = sol.mergeTrees(p, q)
t3 = sol.trim_iter(q, 3, 4)
iter_tree(t3)






