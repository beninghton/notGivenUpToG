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

        prev = head
        curr = head
        head = ListNode(None)
        head.next = prev
        cnt = 0

        while curr != None and curr.next != None:

            if curr.val == curr.next.val:
                curr = curr.next
                prev.next = curr
                cnt += 1
            else:
                if cnt > 0:
                    prev.next = curr.next
                    cnt = 0
                    curr = curr.next
                else:
                    curr = curr.next
                    if curr.next != None:
                        if curr.val != curr.next.val:
                            prev = prev.next






        return head

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
print sol.deleteDuplicates(l1)

sol.print_linked_list(l1)