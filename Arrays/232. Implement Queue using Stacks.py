class MyQueue(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue = []

    # Сложность O(N), т.к. сдвигаем лист каждый раз, когда добавляем элемент. Space - O(N), т.к. перестраиваем стек.
    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: void
        """
        if x:
            if self.queue == []:
                self.queue.append(x)
            else:
                self.queue = [x] + self.queue

    # O(1), O(1)
    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        if self.queue == []:
            print("There is no elements in the list")
        else:
            return self.queue.pop()

    # O(1), O(1)
    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        if self.queue == []:
            print("There is no elements in the list")
        else:
            return self.queue[-1]

    # O(1), O(1)
    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return self.queue == []

    # Сложность  O(N), O(N)



    ### Найдем Более оптимальное решение. Вместо того чтобы при каждом добавлении элемента сдвигать весь лист, мы будем пользоваться append, где amortized O(1)
class MyQueue_2(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        # Используем 2 стека, popper и pusher, для достижения Amortized Time O(1). То есть когда из одного стека в другой будем переливать, тогда время будет O(N), в остальных случаях - O(1)
        self.popper = []
        self.pusher = []

    # O(1), O(n)
    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: void
        """
        if x:
            self.pusher.append(x)

    # O(1) - Amortized. O(1)
    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        # Если popper пустой, значит отдавать нам нечего, и надо перелить из стека pusher в стек pop в обратном порядке.
        if self.popper == []:
            while self.pusher:
                self.popper.append(self.pusher.pop())
            return self.popper.pop()
        else:
            return self.popper.pop()

    # O(1), O(1)
    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        # Допускаем что элементы есть по условию. Возвращаем верхний элемент с popper'a. Если popper пустой - возвращаем первый элемент с пушера.
        if self.popper:
            return self.popper[-1]
        return self.pusher[0]

    # O(1), O(1)
    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        # Если оба стека пустые - возвращаем True. Если один из них полный - возвращаем False.
        return self.popper == [] and self.pusher == []



# Сложность  O(1) - Amortized worst case., O(N)

my_que = MyQueue_2()

my_que.push(5)
x = my_que.pop()
print(x)
#my_que.pop()
#x = my_que.peek()
#print(x)
print(my_que.empty())







