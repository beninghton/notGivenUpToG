class Solution(object):
    def scoreOfParentheses(self, S):
        def F(i, j):
            #Score of balanced string S[i:j]
            ans = bal = 0

            #Split string into primitives
            for k in range(i, j):
                bal += 1 if S[k] == '(' else -1
                if bal == 0:
                    if k - i == 1:
                        ans += 1
                    else:
                        ans += 2 * F(i+1, k)
                    i = k+1

            return ans

        return F(0, len(S))


class Solution2(object):
    # Идем по строке, главное понять, что сколько у нас открытых скобок, и затем закрывать их и либо умножать на 2, либо прибавлять.
    def scoreOfParentheses(self, S):
        ans = bal = 0
        for i, x in enumerate(S):
            if x == '(':
                bal += 1
            else:
                bal -= 1
                if S[i-1] == '(':
                    ans += 1 << bal
        return ans

    def scoreOfParentheses2(self, S):
        ans = bal = 0
        for i, x in enumerate(S):
            if x == '(':
                bal += 1
            else:
                bal -= 1
                if S[i-1] == '(':
                    if bal == 0:
                        ans += 1
                    else:
                        ans += 2 ** bal
        return ans


class Solution:
    def scoreOfParentheses(self, S):
        """
        :type S: str
        :rtype: int
        """
        # https://leetcode.com/problems/score-of-parentheses/solution/
        stack = [0]

        for x in S:
            if x == '(':
                stack.append(0)
            else:
                v = stack.pop()
                stack[-1] += max(v*2, 1)

        return stack.pop()


sol = Solution2()
print(sol.scoreOfParentheses2('(()()())'))