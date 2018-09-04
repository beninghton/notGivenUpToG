class Solution:
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """

        if len(matrix) < 2:
            return True

        # Строка, в которую помещаем сдвигаемые элементы. Они должны быть равны след. строке, начиная с индекса 1.
        shifted = matrix[0][:-1]

        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[i][j] != shifted[j-1]:
                    return False

            # Обновляем shifted каждый раз
            shifted = matrix[i][:-1]

        return True

    # T - O(R*C) - проходм 1 раз по матрице
    # S - O(K), где K = len(matrix[0])


    # Вообще просто
    def isToeplitzMatrix2(self, m):
        for i in range(len(m) - 1):
            for j in range(len(m[0]) - 1):
                if m[i][j] != m[i + 1][j + 1]:
                    return False
        return True

    # O(R*C)
    # O(1)

