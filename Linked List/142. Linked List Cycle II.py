class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None



class Solution(object):

    def detectCycle(self, head):

        fast_p = head
        slow_p = head
        index = head


        while fast_p and fast_p.next:
            slow_p = slow_p.next
            fast_p = fast_p.next.next

            if slow_p == fast_p:
                if slow_p == index or slow_p.next == index:
                    return index.val
                else:
                    index = index.next

        return None

    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        fast_p = head
        slow_p = head
        index = head


        while fast_p and fast_p.next:   # O(N)
            slow_p = slow_p.next
            fast_p = fast_p.next.next

            if slow_p == fast_p:
                while index != slow_p:  # O(N). Суммируются O(N) + O(N) т.к. после достижения  slow_p == fast_p верхний цикл больше не выполняется
                    slow_p = slow_p.next
                    index = index.next
                return index

        return None

    def print_linked_list(self, item):
        # base case
        if item == None:
            return
        # lets print the current node
        print(item.val)
        # print the next nodes
        self.print_linked_list(item.next)


l1 =  ListNode(3)
l1.next = tmp = ListNode(2)
l1.next.next = ListNode(0)
l1.next.next.next = ListNode(-4)
l1.next.next.next.next = tmp
#l1.next.next.next.next = ListNode(4)
#l1.next.next.next.next.next = ListNode(4)
#l1.next.next.next.next.next.next = tmp

sol = Solution()

#sol.deleteDuplicates(l1)
print sol.detectCycle(l1)

#sol.print_linked_list(l1)

# Подход тут https://stackoverflow.com/questions/2936213/explain-how-finding-cycle-start-node-in-cycle-linked-list-work
# Все по формуле, без формулы хер решишь
# Сложность...O(N)