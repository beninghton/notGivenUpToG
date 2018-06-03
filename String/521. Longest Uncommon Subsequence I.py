class Solution(object):
    def findLUSlength(self, a, b):          # O(min(a,b))
        """
        :type a: str
        :type b: str
        :rtype: int
        """


        if len(a) != len(b):
            return max(len(a), len(b))

        else:
            if a in b:
                return -1
            else:
                return len(a)


    def findLUSlength(self, a, b):          # O (N^2), space complexity - O(N)
        """
        :type a: str
        :type b: str
        :rtype: int
        """
        """ One approach seems to be:
            For every character, generate all subsequences
            and it is already present in this string but 
            check if it is *not* present in the other.
            That will make it one of the eligible ones.
            Complexity will be kinda big: N**2 right?
            For each character, we will do N subsequences.
            An optimization could be that we store subsequences
            we have already seen in a set
            This way, we dont see it again
        """

        maxS = 0
        subsequences_seen = set([])

        for i in range(len(a)):                 # O(N), N = len(a)
            for j in range(i+1,len(a)+1):
                print a[i:j]
                if a[i:j] not in b:             # O(N), N = size of slice
                    if len(a[i:j]) > maxS:
                        maxS = len(a[i:j])
                        subsequences_seen.add(maxS)



        for i in range(len(b)):                 # O(N), N = len(b)
            for j in range(i+1,len(b)+1):
                print b[i:j]
                if b[i:j] not in a:             # O(N), N = size of slice
                    maxS = len(b[i:j])
                    subsequences_seen.add(maxS)

        if len(subsequences_seen) > 0:
            return max(subsequences_seen)
        else:
            return -1

sol = Solution()

a = "abc"
b = "rbd"
print (sol.findLUSlength(a, b))




