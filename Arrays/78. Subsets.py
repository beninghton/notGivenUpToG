class Solution:
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        ans = []
        ans.append([])


        def helper(temp_nums, start, end):

            # Дальше идем от этого индекса.
            for i in range(start, end):
                # При каждой итерации мы копируем лист заново, добавляем в него новый элемент.
                # Копирование нужно, чтобы каждый раз лист обнулялся, добавляя новый элемент по индексу.
                temp = temp_nums.copy()
                temp.append(nums[i])

                # Далее добавляем его в ответ, и снова вызываем хелпер, увеличивая стартовый индекс.
                ans.append(temp)
                helper(temp, i + 1, end)


        # Идем по списку, берем каждый его элемент и добавляем в массив. Дальше вызываем хелпер, но список увеличиваем на
        for i in range(len(nums)):
            ans.append([nums[i]])
            helper([nums[i]], i + 1, len(nums))


        return ans


# Количество subsets - 2^N, N - number of items in nums.
# T- O(N*2^N). Для каждого N делаем subset. А вот когда делаем копию, непонятно...
# S - O(N*2^N). Так же когда делаем копию, и при вызове хелпера мы тоже как бы делаем копию каждого элемента.
# Получается как бы во время copy - 1 вариант, дальше helper - 2 варинат, и поэтому 2^N.

# от Сергея:
# Time complexity -  O(n*2^n)
# space complexity O(n) +  /stack because of recursion/ +  O(n*2^n) =>  O(n*2^n)
# number of arrays is 2^n.


    # Тоже решение, но не копируем лист при итерации, а копируем, когда кладем в ans. По сути, та же фигня.
    def subsets2(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        ans = []
        ans.append([])


        def helper(temp_nums, start, end):

            # Дальше идем от этого индекса.
            for i in range(start, end):
                # Сначала добавляем
                temp_nums.append(nums[i])

                # Затем отдаем копию в ans. Если мы отдадим не копию, а ссылку на лист, то далее она будет внутри ANS так же меняться.
                # Поэтому мы как бы даем ссылку на копию, которая меняться не будет.
                ans.append(temp_nums.copy())
                helper(temp_nums, i + 1, end)

                # В конце убираем то что добавили, для сохранения листа.
                temp_nums.pop()


        # Идем по списку, берем каждый его элемент и добавляем в массив. Дальше вызываем хелпер, но список увеличиваем на
        for i in range(len(nums)):
            ans.append([nums[i]])
            helper([nums[i]], i + 1, len(nums))


        return ans



# Интересно решение - https://leetcode.com/problems/subsets/discuss/122645/3ms-easiest-solution-no-backtracking-no-bit-manipulation-no-dfs-no-bullshit

    # Super Short, AMAZING.
    def subsets3(self, nums):
        nums.sort()
        result = [[]]
        for num in nums:
            result += [i + [num] for i in result]
        return result



sol = Solution()

candidates = [1,2,3]


print(sol.subsets3(candidates))
