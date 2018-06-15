# -*- coding: utf-8 -*-
# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution:
    def numComponents(self, head, G):
        """
        :type head: ListNode
        :type G: List[int]
        :rtype: int
        """

        cnt = 0
        flag = False
        set_g = set(G)

        while head is not None:
            while head is not None and head.val in set_g:
                set_g.remove(head.val)
                head = head.next
                flag = True

            if flag:
                cnt += 1
                flag = False

            if head is not None:
                head = head.next

        return cnt


    def numComponents_leetcode(self, head, G):
        Gset = set(G)
        cur = head
        ans = 0
        while cur:
            if (cur.val in Gset and
                        getattr(cur.next, 'val', None) not in Gset):
                ans += 1
            cur = cur.next

        return ans

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
G = [0, 3, 1, 4]

print sol.numComponents(l1, G)


# O(N), хотя leetcode утверждает, что time complexity O(N+G.lenght), where N is the length of the linked list with root node head.
# O(G), G - lenght of elements in G
