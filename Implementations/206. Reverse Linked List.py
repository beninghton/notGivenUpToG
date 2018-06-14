# -*- coding: utf-8 -*-
class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None


class Solution(object):
    def reverseList_iterative(self, head):          # O(N), O(1)
        """
        :type head: ListNode
        :rtype: ListNode
        """
        curr = head
        prev = None

        if head is None or head.next is None:
            return head

        while curr is not None:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp

        return prev

    def print_linked_list(self, item):
        # base case
        if item == None:
            return
        # lets print the current node
        print(item.val)
        # print the next nodes
        self.print_linked_list(item.next)

    def reverseList(self, head):            # O(N), O(N) - https://leetcode.com/problems/reverse-linked-list/solution/
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head

        p = self.reverseList(head.next)     # Доходим до посл элемента, p - становится последним, его мы и вернем как head


        head.next.next = head               # Head начинает отсчет назад, и мы меняем next'ы, чтобы след смотрел на пред. head
        head.next = None                    # Обнуляем head.next текущего

        #print p.val
        return p                            # Возвращаем p, он же head реверсного листа

    def rec(self, l, i):            # Функция для обычного листа, O(N), O(1)
        if i == len(l):
            return []               # 2. Если дошли, значит индекс равен длине, возвращаем пустой лист

        x = self.rec(l, i+1)        # 1. Идем до конца листа, ждем пока дойдем до посл элемента

        x.append(l[i])              # 3. Добавляем в пустой лист наш посл элемент, затем предпоследний и т.д.
        return x



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
sol.print_linked_list(sol.reverseList(l1))

'''
1. Iterative - O(N), O(1). Меняем In-Place.
'''


l = [1,2,3]
i = 0
print sol.rec(l,i)