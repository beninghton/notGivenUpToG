class Solution(object):
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """

        map = {}
        map["L"] = 0

        for i in range(len(s)):
            if s[i] == "A":

                map["L"] = 0

                if "A" in map:
                    return False
                else:
                    map["A"] = 1

            elif s[i] == "L":
                if map.get("L") > 2:
                    return False
                else:
                    map["L"] += 1
                    if map.get("L") > 2:
                        return False
            else:
                map["L"] = 0

        return True

    def checkRecordOpt(self, s):

        if s.count("A") > 1:
            return False

        if "LLL" in s:
            return False

        return True










sol = Solution()

#s1 = "PPALLP"
s2 = "LPLPLPLPLPL"

#print sol.checkRecord(s1)
print sol.checkRecordOpt(s2)