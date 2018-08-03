class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        # Вытащим оба числа с обоих листов, перевернем их и сложим. Решение типа brute-force.
        number1 = []
        number2 = []

        while l1 is not None:
            # Добавляем сразу конвертируя в строку
            number1.append(str(l1.val))
            l1 = l1.next

        while l2 is not None:
            number2.append(str(l2.val))
            l2 = l2.next

        # Переворачиваем числа и вычисляем сумму. Ее переворачивать не будем, т.к. она засунется в линкед лист и так наоборот.

        number1 = ''.join(number1[::-1])
        number2 = ''.join(number2[::-1])

        summ = str(int(number1) + int(number2))

        # Засовываем сумму в новый лист, не забывая конвертнуть в инт обратно.
        # Фиксируем head, и дальше на него ссылаемся в цикле
        head = ListNode(int(summ[0]))

        for i in range(1, len(summ)):
            node = ListNode(int(summ[i]))
            node.next = head
            head = node

        return head

# T - O(N+M), where N and M - count of nodes in both numbers
# S - O(N+M) - для хранения этих символов используем листы. И строки.


    # Элегантное решение без переворачивания и конвертации
    def addTwoNumbers_elegant(self, l1, l2):

        carry = 0
        # Иницализируем новый лист, где dummy это None, а след это будет корень нового листа, который и будем возвращать.
        dummy = n = ListNode(None)

        # Идем по обоим листам пока есть ноды в одном из листов или есть carry. Добавляем одновременно в две ноды
        while l1 or l2 or carry:
            if l1:
                # Добавляем сначала левую ноду к кери
                carry += l1.val
                l1 = l1.next
            if l2:
                # Потом правую
                carry += l2.val
                l2 = l2.next

            # Берем целое и остаток от керри(сумма двух чисел). В carry пойдет целое, в remainder - остаток.
            carry, remainder = divmod(carry, 10) # the same as (a // b, a % b)
            # Остаток пишем в новую ноду, и переключаемся на нее.
            n.next = ListNode(remainder)
            n = n.next
        return dummy.next

#Complexity Analysis

#Time complexity : O(max(m,n)). Assume that m and n represents the length of l1 and l2 respectively, the algorithm above iterates at most max(m,n) times.

#Space complexity : O(max(m,n)). The length of the new list is at most max(m,n)+1.



l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)

sol = Solution()

l3 = sol.addTwoNumbers_elegant(l1, l2)

while l3 is not None:
    print(l3.val)
    l3 = l3.next
