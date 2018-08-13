import heapq


# Time limit exceeded
class KthLargest(object):

    # T - O(N*LogN) - heapify. S - O(N) - list. N - длина листа.
    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        # Окучиваем лист (в возраст порядке)
        heapq.heapify(nums)

        self.nums = nums
        self.k = k

   # T - O(N*LogK)
    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        heapq.heappush(self.nums, val)

        try:
            # Возвращаем элемент из листа k-больших элементов.
            return heapq.nlargest(self.k, self.nums)[self.k - 1]
            #return nums[k-1]
        except:
            print("No such Kth element in the queue")




class KthLargest2(object):

    # T  O(N*LogN) + O((n-k) log n) = O(N*Log(N)) -- добавляем в кучу heapq.
    # S - O(N) - лист.
    def __init__(self, k, nums):
        self.pool = nums
        self.k = k
        self.size = len(self.pool)
        # В результате heapify НЕ обязательно что все будет отсортировано. Просто минимальный элемент переместится в начало.
        heapq.heapify(self.pool)    # O(N*LogN)to push all the items onto the heap

        # Оставляем 3 максимальных элемента в листе
        while self.size > k: # O((n-k) log n) to find the kth largest element
            # Убираем каждый раз минимальный элемент, тем самым K наибольших элемента останутся в листе. И минимальный будет как раз K-ым.
            heapq.heappop(self.pool)
            self.size -= 1

    # T - O(Log(K)) - потому что в листе щас только K элементов находится. Push, replace - это Log(K).
    # S - O(1) - дополнительно не используем место, кроме как 1 раз добавить элемент если длина листа меньше k.
    def add(self, val):
        # Сдесь проверяем если размер листа меньше k (а это может быть только на один, например пустой лист [], и 1-й элемент (len=0, k= 1))
        # Тогда добавляем его в кучу. Прибавляем size. Возвращать тогда будем тоже его.
        if self.size < self.k:
            heapq.heappush(self.pool, val)
            self.size += 1
        # Если с сайзом все ок, и значение больше, реплейсим минимальный элемент на новый, как бы длина листа не меняется.
        # Просто минимальный выпиливаем, и новый встает на нужное место.
        elif val > self.pool[0]:
            # Возвращаем новый минимальный(первый) элемент (он же k-th largest)
            heapq.heapreplace(self.pool, val)
        # В любом случае возвращаем первый элемент(он же k-th largest)
        return self.pool[0]



nums = [3,2,3,1,2,8]
k = 9999
# Your KthLargest object will be instantiated and called as such:
obj = KthLargest2(k, nums)
param_1 = obj.add(10)
print(param_1)

"""
We can build a MinHeap that contains only k largest elements.
On add:

compare a new element x with min to decide if we should pop min and insert x
take into account a case when heap_size is less than k
Construction is simply calling the add function N times.

Time complexity:

Construction: O(N * logK)
Adding: O(logK)
Additional memory:

O(K) (can be reduced to O(1) by reusing memory of the existing array)
Have fun!
"""