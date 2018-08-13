class Solution:
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        ans = []

        def helper(res, target, candidates):

            # Base case, если ушли таргетом меньше нуля.
            if target < 0:
                return

            # только если таргет 0, значит сумма есть, добавляем.
            if target == 0:
                # Добавляем копию res, иначе если добавить переменную res (ссылку на лист) и дальше будем менять этот лист res, он изменится, находясь в ans.
                ans.append(res.copy())
                return

            else:
                # Идем по листу и добавляем в локальный результат значения, которые проходим. Отнимая их от таргета.
                # Для того чтобы избежать дубликатов, передаем не полный лист, а его копию, исключая индексы, которые мы уже прошли.
                # Для того чтобы res держать в актуальном состоянии, оттуда нужно удалять элементы в конце.
                for i in range(len(candidates)):
                    res.append(candidates[i])
                    helper(res, target - candidates[i], candidates[i:])
                    res.remove(candidates[i])



        helper([], target, candidates)


        return ans



sol = Solution()

candidates = [1,2,3,4,5,6,7,8,9,10]
target = 10


print(sol.combinationSum(candidates, target))

# T -  O(k * 2 ^ n), where k is the average length of all the combinations and n is the size of nums

# Another version
# This algorithm has time complexity O((n+k)!) where n is the size of candidates, and k is the max repeated times for each candidates

#space complexity O(m) where m is the size of array for the solution.