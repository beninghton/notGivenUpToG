# -*- coding: utf-8 -*-

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        if len(strs) == 0:
            return ""

        prefix = strs[0]

        for word in strs:

            while word.find(prefix) != 0:
                prefix = prefix[0:len(prefix)-1]
                if not prefix:
                    return ""

        return prefix



    def opt(self,strs):         ### Сдесь нашел общий максимальный элемент(подстроку) во всех строках
        if strs == []:
            return []

        #strs.sort(key=len)     ## Если закоментить тут

        l0 = len(strs[0])
        s0 = strs[0]
        cnt = 0

        while l0 >= 0:
            for i in range(1,len(strs)):
                if strs[i][:l0].find(s0[:l0]) != -1:        # И поставить strs[i][:l0] вместо strs[i] тогда получим решение.
                    cnt +=1                                 # Если не комментить, тогда будет искать не в префиксе, а в целом слове
                else:
                    cnt = 0
                    l0 -= 1
                    break

            if cnt > 0:
                return s0[:l0]

                #l0 -= 1


sol = Solution()

print (sol.longestCommonPrefix(["ca","a"]))
print (sol.opt(["c","acc","ccc"]))


# Смысл алгоритма - берем первое слово за префикс и сокращаем его с конца, сравнивая с другими
# Сложность - O(N*S) - N - количество элементов, S - сумма всех строк