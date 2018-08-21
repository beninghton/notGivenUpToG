class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """

        ans = []
        i = 1

        # generate the list
        while i < numRows + 1:
            if i == 1:
                ans.append([1])
            elif i == 2:
                ans.append([1, 1])
            else:
                # Define local list. По краям у нас [1]. Добавляем вначале и в конце. Цикл соответственно - между.
                l = [1]
                for k in range(1, i - 1):
                    sum = ans[i - 2][k - 1] + ans[i - 2][k]
                    l.append(sum)
                l.append(1)
                ans.append(l)
            i += 1

        return ans

# T - O(N^2), N - numrows
# S - O(N^2), internal list and answer

    # Тоже решение, просто код более красивый, наверное...
    def generate_leetcode(self, num_rows):
        triangle = []

        for row_num in range(num_rows):
            # The first and last row elements are always 1.
            row = [None for _ in range(row_num+1)]
            row[0], row[-1] = 1, 1

            # Each triangle element is equal to the sum of the elements
            # above-and-to-the-left and above-and-to-the-right.
            for j in range(1, len(row)-1):
                row[j] = triangle[row_num-1][j-1] + triangle[row_num-1][j]

            triangle.append(row)

        return triangle


sol = Solution()
print(sol.generate(5))


