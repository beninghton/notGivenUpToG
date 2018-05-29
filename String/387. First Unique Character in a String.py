class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """

        if s == "":
            return -1

        if len(s) == 1:
            return 0

        temp = []

        for i in range(len(s)-1):
            if s[i] not in temp and s[i] not in s[i+1:]:
                return i

            temp.append(s[i])

        if s[-1] not in temp:
            return len(s)-1
        else:
            return -1

    def firstUniqCharOpt(self, s):
        if s == "":
            return -1
        if len(s) == 1:
            return 0

        temp = []

        if len(s)==0:
            return -1
        alph = string.ascii_lowercase   # alphabet

        for ch in alph:                 # iterate through alphabet, if find index, put it in the temp list
            if s.count(ch) == 1:
                temp.append(s.index(ch))


        if len(temp)!=0:
            return min(temp)           # find the min index in the list (first occurence)
        else:
            return -1



sol = Solution()

s = "loveleetcode"
print (sol.firstUniqCharOpt(s))
print (sol.firstUniqChar(s))

