# -*- coding: utf-8 -*-
class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None



class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """

        currA = headA

        while currA:

            currB = headB
            while currB:
                if currA == currB:
                    return currA.val
                else:
                    currB = currB.next

            currA = headA.next
            headA = headA.next

        return None

    def getIntersectionNode_set(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """

        currA = headA
        currB = headB
        s = set()

        while currA:
            s.add(currA)
            currA = currA.next

        while currB:
            if currB in s:
                return currB
            else:
                currB = currB.next


        return None

    def getIntersectionNode_2pointers(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """

        currA = headA
        currB = headB

        while currA is not currB:

            if currA is None:
                currA = headB
            else:
                currA = currA.next

            if currB is None:
                currB = headA
            else:
                currB = currB.next

        return currA


l1 =  ListNode(3)
l1.next = tmp = ListNode(2)
l1.next.next = ListNode(0)
l1.next.next.next = ListNode(-4)
#l1.next.next.next.next = tmp
#l1.next.next.next.next = ListNode(4)
#l1.next.next.next.next.next = ListNode(4)
#l1.next.next.next.next.next.next = tmp

l2 = ListNode(2)
l2.next = ListNode(8)
l2.next.next = l1.next.next

sol = Solution()


print sol.getIntersectionNode(l1,l2)

'''

1. O(M*N), O(1) итерируем по каждому, ждем пока будут равны - значит перемещение началось. M и N - длины списков до пересечения
2. O(M + N), O(N) or O(M) - с сетом.
3. 2 pointers: когда доходим до конца одной ветки - переключаем поинтер ее на начало другой. Они все равно будут равны друг
другу либо на None либо на пересечении. Т.к. оба проходят тоже самое расстояние, сначала одну ветку потом другую.
# the idea is if you switch head, the possible difference between length would be countered. 
# On the second traversal, they either hit or miss. 
# if they meet, currA or currB would be the node we are looking for, 
# if they didn't meet, they will hit the end at the same iteration, currA == currB == None, return either one of them is the same,None

'''

