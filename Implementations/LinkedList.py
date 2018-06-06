class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None



class LinkedList(object):
    def __init__(self):
        self.head = None
        self.size = 0

    def append(self, data):
        if self.head == None:
            self.head = Node(data)
            self.size += 1
        else:
            currNode = self.head
            newNode = Node(data)
            while currNode.next != None:
                currNode = currNode.next
            currNode.next = newNode
            self.size += 1

    def display(self):
        currNode = self.head
        if not currNode:
            print None
        else:
            while(currNode):
                if currNode.next == None:
                    print '{} -> {}'.format(currNode.data, currNode.next)
                else:
                    print '{} ->'.format(currNode.data),
                currNode = currNode.next


    def prepend(self, data):
        newHead = Node(data)
        newHead.next = self.head
        self.head = newHead
        self.size += 1

    def find(self, data):
        currNode = self.head
        while True:
            if currNode.data == data:
                return data
            currNode = currNode.next
        return None


    def remove(self, data):
        currNode = self.head

        if currNode.data == data:
            self.head = currNode.next
            return
        while currNode.next != None:
            if currNode.next.data == data:
                currNode.next = currNode.next.next
                return
            currNode = currNode.next

'''
    def remove(self, data):
        currNode = self.head
        prev = None
        while currNode != None:
            if currNode.data == data:
                if currNode == self.head:
                    self.head = currNode.next
                    return
                else:
                    prev.next = currNode.next
                    return

            prev = currNode
            currNode = currNode.next
'''

n = LinkedList()
n.display()
n.append(6)
n.display()
n.append(10)
n.display()
n.append(30)
n.display()
n.prepend(999)
n.display()
print "Lenght is " + str(n.size)
print n.find(10)
n.remove(10)
n.display()

