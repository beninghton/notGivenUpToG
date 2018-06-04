class Solution(object):
    def canConstruct(self, ransomNote, magazine):       # O(N + K)
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """

        map_mag = {}
        map_rans = {}

        for ch in magazine:
            if ch in map_mag:
                map_mag[ch] += 1
            else:
                map_mag[ch] = 1


        for ch in ransomNote:
            if ch not in map_mag:
                return False
            else:
                if ch in map_rans:
                    map_rans[ch] += 1
                else:
                    map_rans[ch] = 1

        for ch in ransomNote:
            if map_mag[ch] < map_rans[ch]:
                return False

        return True

    def canConstructOpt(self, ransomNote, magazine):        # O(N+ K) тупо через count, N - кол-во символов Magazine. Space - O(N)
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        for i in set(ransomNote):                           # В результате после сета будет 30 букв, это константа O(1), но что бы преобразовать в сет нужно пройти каждую букву. Значит O(N).
            if ransomNote.count(i) > magazine.count(i):     # Сначала преобразовал в set, затем пошел по нему. O(N) - цена преобразования, где N - кол-во символов в ransomNote
                return False                                # Count - каждый символ - O(K), где K - кол-во символов в магазине
        return True


sol = Solution()


print (sol.canConstruct("abab", "aaba"))




