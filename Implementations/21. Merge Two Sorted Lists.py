class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None


class Solution(object):
    def mergeTwoLists_Recursive(self, l1, l2):              # Recursive solution, O(N+K), O(N)

        if not l1 or not l2:
            return l1 or l2

        if l1.val <= l2.val:
            l = ListNode(l1.val)
            l.next = self.mergeTwoLists_Recursive(l1.next, l2)

        elif l1.val > l2.val:
            l = ListNode(l2.val)
            l.next = self.mergeTwoLists_Recursive(l1, l2.next)


        return l

    def mergeTwoLists_Iterative(self, l1, l2):              # Берем за начальную ноду нулевую, затем от нее строим новую, по порядке, выбирая либо ноду l1, либо l2. O(N+K)


        head = curr = ListNode(None)

        while l1 and l2:
            if l1.val <= l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next

            curr = curr.next

        curr.next = l1 if l1 else l2                    # Если одна из нод кончится, добавляем ту, которая еще есть
        return head.next                                # В конце отсекаем начальную нулевую ноду и возвращаем лист



        # in-place, iteratively
    def mergeTwoLists(self, l1, l2):
        if None in (l1, l2):
            return l1 or l2
        dummy = cur = ListNode(0)
        dummy.next = l1
        while l1 and l2:
            if l1.val < l2.val:
                l1 = l1.next
            else:
                nxt = cur.next
                cur.next = l2
                tmp = l2.next
                l2.next = nxt
                l2 = tmp
            cur = cur.next
        cur.next = l1 or l2
        return dummy.next

l1 = ListNode(1)
l1.next = ListNode(2)
l1.next.next = ListNode(4)

l2 = ListNode(1)
l2.next = ListNode(3)
l2.next.next = ListNode(4)

sol = Solution()

sol.mergeTwoLists_Recursive(l1,l2)
sol.mergeTwoLists_Iterative(l1,l2)