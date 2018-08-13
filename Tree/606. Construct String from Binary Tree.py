# -*- coding: utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


"""
Input: Binary tree: [1,2,3,4]
       1
     /   \
    2     3
   /    
  4     

Output: "1(2(4))(3)"

Input: Binary tree: [1,2,3,null,4]
       1
     /   \
    2     3
     \  
      4 

Output: "1(2()(4))(3)"
"""



class Solution:



    def tree2str(self, t):
        """
        :type t: TreeNode
        :rtype: str
        """

        ans = []
        count = 0

        def helper(t, ans, count):
            if t is None:
                return

            # Добавляем сначала открытую скобку, потом значение, и увеличиваем счетчик открытых скобок.
            ans.append('(')
            ans.append(str(t.val))
            count += 1

            # Если нет левой но есть правая, добавляем пустышку
            if t.left is None and t.right:
                ans.append('()')

            # Проходим по дереву
            helper(t.left, ans, count)
            helper(t.right, ans, count)

            # Смотрим если открытые скобки есть, добавляем закрытую. (1 не причем, т.к. она первая добавилась и мы уберем ее в конце)
            if count > 1:
                ans.append(')')
                count -= 1


        helper(t, ans, count)

        return ''.join(ans[1:])



#Time complexity : O(n). The preorder traversal is done over the n nodes of the given Binary Tree.
#Space complexity : O(n). The depth of the recursion tree can go upto n in case of a skewed tree.



t = TreeNode(1)
t.left = TreeNode(2)
t.right = TreeNode(3)
sol = Solution()
print(sol.tree2str(t))


# C leetcode 1
class Solution2:
    def tree2str(self, t):
        res = []
        self.helper(t, res)
        return "".join(res)

    def helper(self, node, res):
        if node:
            res.append(str(node.val))
            if node.left or node.right:
                res.append("(")
                self.helper(node.left, res)
                res.append(")")
                if node.right:
                    res.append("(")
                    self.helper(node.right, res)
                    res.append(")")

# C leetcode 2
class Solution3:
    def tree2str(self, t):
        """
        :type t: TreeNode
        :rtype: str
        """

        return self.helper(t)

    def helper(self, t):

        if not t:
            return ''

        left = self.helper(t.left)
        right = self.helper(t.right)

        if not left and not right:

            return str(t.val)


        if not left:

            return str(t.val)  +  '()' + '(' + right + ')'

        if not right:

            return str(t.val) + '(' + left + ')'

        return str(t.val) + '(' + left + ')' + '(' + right + ')'

sol2 = Solution3()
print(sol2.tree2str(t))