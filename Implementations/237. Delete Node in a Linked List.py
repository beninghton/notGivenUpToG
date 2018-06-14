# -*- coding: utf-8 -*-
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next




l1 =  ListNode(1)
l1.next = tmp = ListNode(2)
l1.next.next = ListNode(3)
l1.next.next.next = ListNode(4)
#l1.next.next.next.next = tmp
#l1.next.next.next.next = ListNode(4)
#l1.next.next.next.next.next = ListNode(4)
#l1.next.next.next.next.next.next = tmp

l2 = ListNode(2)
l2.next = ListNode(8)
l2.next.next = l1.next.next

sol = Solution()


#print sol.reverseList(l1)
#sol.print_linked_list(sol.reverseList(l1))

'''
1.  O(1), O(1). Меняем In-Place одноразово. Копируем знач след ноды себе и игнорим след ноду.
'''


l = [1,2,3]
i = 0
print sol.rec(l,i)