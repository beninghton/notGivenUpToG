class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None


class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """


        curr = head
        while curr != None and curr.next != None:
            if curr.next.val == curr.val:
                curr.next = curr.next.next

            else:
                curr = curr.next

        return head


# Идем по листу, если curr элемент == next элемент, "прыгаем" через него. И указываем на тот что после него. Сам head не двигаем
# Если next элемент другой, тогда двигаем хеад дальше, а возвращаем голову tmp
# O(N), O(1)


l1 = ListNode(1)
l1.next = ListNode(1)
l1.next.next = ListNode(1)
#l1.next.next.next = ListNode(3)
#l1.next.next.next.next = ListNode(3)

l2 = ListNode(1)
l2.next = ListNode(1)
l2.next.next = ListNode(2)

sol = Solution()

#sol.deleteDuplicates(l1)
print sol.deleteDuplicates(l1)