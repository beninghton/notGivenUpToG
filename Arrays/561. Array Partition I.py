class Solution:
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        nums.sort()
        total = 0
        for i in range(0, len(nums), 2):
            total += nums[i]
        return total

    def arrayPairSum_mine(self, nums):

        array = [0]*20
        total = 0

        for el in nums:
            array[el+10] += 1

        even = False
        index = 0

        for i,freq in enumerate(array):

            while freq > 0:
                if even:
                    total += index - 10
                    even = False
                    freq -= 1
                else:
                    even = True
                    index = i
                    freq -= 1

        return total

    def arrayPairSum_elegant(self, nums):
        array = [0]*20
        total = 0

        for el in nums:
            array[el+10] += 1

        odd = True

        for i,freq in enumerate(array):

            while freq > 0:
                if odd:
                    total += i - 10

                odd = not odd
                freq -= 1


        return total


sol = Solution()




print(sol.arrayPairSum_math([1,2,3,2]))

### .1 O(NlogN) , O(logN) - спейс для сортировки. Например quicksort.
# Просто берем каждый второй элемент

# 2.O(K), O(K), where K is the range of the numbers.
# Создаем массив с индексами для всех возможных значений элементов оригинального массива.
# Т.е. элемент в одном массиве равен индексу в другом. Т.к. рендж элементов [-10000,10000] то создаем массив с 20001 эл-ом(от - до + и еще 0)
# в этом массиве элементы хэшируем как бы, добавляя единицу к соотв номеру индекса
# Если есть дупликаты, так же добавляем единицу.
# Элегантный спосо- просто перещелкиваем odd и добавляем либо не добавляем.
