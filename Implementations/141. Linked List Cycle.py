# -*- coding: utf-8 -*-
class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None



class Solution(object):
    def hasCycle(self, head):

        s = set()
        s.add(head)
        while head and head.next != None:
            if head.next in s:
                return True
            else:
                s.add(head)
                head = head.next
        return False

    def hasCycle_visited(self, head):

        while head and head.next != None:
            head.val = "visited"
            if head.next.val == "visited":
                return True
            else:
                head = head.next
        return False

    def hasCycle_Floyd(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """


        slow_p = head
        fast_p = head

        while fast_p and fast_p.next:
            slow_p = slow_p.next
            fast_p = fast_p.next.next
            if slow_p == fast_p:
                return True

        return False

    def print_linked_list(self, item):
        # base case
        if item == None:
            return
        # lets print the current node
        print(item.val)
        # print the next nodes
        self.print_linked_list(item.next)


l1 = ListNode(1)
l1.next = ListNode(2)
l1.next.next = ListNode(3)
l1.next.next.next = ListNode(3)
l1.next.next.next.next = ListNode(4)
l1.next.next.next.next.next = ListNode(4)
l1.next.next.next.next.next.next = ListNode(5)

sol = Solution()

#sol.deleteDuplicates(l1)
print sol.hasCycle_Floyd(l1)

#sol.print_linked_list(l1)

#1. O(N), O(N). Идем по листу и добавляем в сет каждую ноду. Если next нода уже в сете - значит мы в кольце - Return True.
# Иначе False.

#2. O(N), O(1). Visited method - идем по листу и ставим значения в visited. Если уже был visited - значит loop.

#3. O(N), O(1). Floyd method. 2 поинтера. 1 фаст другой slow. Fast прыает на 2 вперед, и если мы в кольце всегда допрыгает до slow.
# O(N) - потому что fast может быть в 2 N,3N и т.д. это все равно O(N)