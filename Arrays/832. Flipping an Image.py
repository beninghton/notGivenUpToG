class Solution:
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """

        if A == []:
            return []

        for i in range(len(A)):
            A[i] = A[i][::-1]

            for j in range(len(A[i])):
                if A[i][j] == 1:
                    A[i][j] = 0
                else:
                    A[i][j] = 1

        return A


sol = Solution()

print(sol.flipAndInvertImage([[1,1,0],[1,0,1],[0,0,0]]))

# T - O(N) - n - кол-во всех элементов
# S - O(K) - k = len(A[i]). Одну строку держим в памяти когда конвертим.


class Solution(object):
    def flipAndInvertImage2(self, A):
        for row in A:
            for i in range((len(row) + 1) // 2):
                """
                In Python, the shortcut row[~i] = row[-i-1] = row[len(row) - 1 - i]
                helps us find the i-th value of the row, counting from the right.
                """
                row[i], row[~i] = row[~i] ^ 1, row[i] ^ 1
        return A


# T - O(N) - n - кол-во всех элементов
# S - O(1) - in place
