class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None


class Solution:
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """

        # Регистрируем dummy ноду, чтобы исключить если главная нода с val, который нужно удалить
        dummy = ListNode(None)
        dummy.next = head

        # Сразу если head пустой, исключаем это
        if head is None:
            return None

        # Пока есть след элемент, сравниваем его значение, если это он - пропускаем его. Если нет - двигаемся дальше.
        while head.next:
            if head.next.val == val:
                head.next = head.next.next
            else:
                head = head.next

        # В конце сравниваем если наш элемент после dummy(он же изначальный head) содержит val для удаления, пропускаем его.
        # Иначе, возвращаем его.
        if dummy.next.val == val:
            return dummy.next.next
        else:
            return dummy.next


# T - O(N)
# S - O(1)

    # Такое же решение, просто немного другое.
    def removeElements2(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        # Сначала пробиваем до конца если у нас head оказался с нужным val.
        while head and head.val == val:
            head = head.next

        if head is None:
            return head

        # После того как наткнулись на нормальное значение, используем prev curr поинтеры.
        prev, curr = head, head.next
        while curr:
            if curr.val == val:
                prev.next = curr.next
            else:
                prev = curr

            curr = curr.next

        return head

l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)

sol = Solution()

l3 = sol.removeElements(l1)

while l3 is not None:
    print(l3.val)
    l3 = l3.next
