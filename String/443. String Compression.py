class Solution(object):
    def compress(self, chars):                  # Requires O(N) space complexity
        """
        :type chars: List[str]
        :rtype: int
        """

        temp, cnt, res = chars[0], 1, []

        for i in range(1, len(chars)):

            if chars[i] == temp:
                cnt += 1
                temp = chars[i]
            else:
                res.append(temp)

                if cnt != 1:
                    for k in str(cnt):
                        res.append(str(k))

                cnt = 1
                temp = chars[i]

        res.append(temp)

        if cnt != 1:
            for k in str(cnt):
                res.append(str(k))

        return res


    def compressOpt(self, chars):               # Requires O(1) space complexity

        anchor, write = 0, 0

        for read, _ in enumerate(chars):

            if read + 1 == len(chars) or chars[read] != chars[read+1]:

                chars[write] = chars[anchor]
                write += 1

                if read - anchor > 1 or read + 1 == len(chars):
                    for d in str(read - anchor + 1):
                        chars[write] = d
                        write += 1


                anchor = read + 1

        return write







sol = Solution()

s = ["a","b","b","b","b","b","b","b","b","b","b","b","b","c","c"]
#s = ["a","a","b","b","c","c","c"]
#s = ["a","b","c","c"]
#print (sol.compress(s))

res = []
for i in range(sol.compressOpt(s)):
    res.append(s[i])

print res
