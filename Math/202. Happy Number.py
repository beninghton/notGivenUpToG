cycle = 0
class Solution(object):

    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """

        # Define storage for the result
        res_set = set()
        res_map = dict()


        while True:
            # Define local_result for the summ
            local_res = 0

            # Переводим в строку для итерации
            # Count all elements, возводим в степень.
            for el in str(n):
                if el not in res_map:
                    res_map[el] = int(el) ** 2
                    local_res += res_map[el]
                else:
                    local_res += res_map[el]


            # Если результат в мапе - мы в кольце, возвращаем False.
            if local_res in res_set:
                return False
            # Иначе идем дальше, и так пока либо не попадем в кольцо либо единица выплывет.
            else:
                if local_res == 1:
                    return True
                else:
                    res_set.add(local_res)
                    n = local_res


        # Решение попроще
    def isHappy_simpler_leetcode(self, n):
        mem = set()
        while n != 1:
            n = sum([int(i) ** 2 for i in str(n)])
            if n in mem:
                return False
            else:
                mem.add(n)
        else:
            return True


    #Floyd's Cycle detection algorithm
    # Как с Linked List, берем 2 разных поинтера и пускаем их с разной скоростью пока не пересекутся.

    def isHappy_floyd(self, n):

        #cycle = 0

        # Helper will be act like main algorithg, it will be separate and divide. Однократно.
        def helper(n):
            # Сумма квадратов цифр, из которых состоит n.
            global cycle
            cycle += 1
            res = sum([int(x) ** 2 for x in str(n)])
            return res

        # Определеим slow и fast. Slow будет вызывать helper однократно, и fast -двухкратно.
        slow = helper(n)
        fast = helper(helper(n))

        # Дальше Вызывать хелпера уже будем в бесконечном цикле. Пока fast != slow или
        while True:
            slow = helper(slow)
            fast = helper(helper(fast))

            # Если fast догнал slow и получил то же значение - значит мы в кольце.
            if fast == slow:
                print(cycle)
                return False
            # Или если один из них в итоге пришел к 1 - возвращаем True.
            if fast == 1 or slow == 1:
                print(cycle)
                return True


sol = Solution()
print(sol.isHappy_floyd(2))

# O(1), O(1), скорее всего пересечение будет примерно в числах до 1000 в любом случае. Какое бы входное число не было. Сет также константный.