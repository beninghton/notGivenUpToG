class MagicDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.magic_set = set()


    def buildDict(self, dict):
        """
        Build a dictionary through a list of words
        :type dict: List[str]
        :rtype: void
        """
        if dict:
            for word in dict:
                self.magic_set.add(word)


    def search(self, word):
        """
        Returns if there is any word in the trie that equals to the given word after modifying exactly one character
        :type word: str
        :rtype: bool
        """

        if word:
            for s in self.magic_set:
                # Если длины не равные сразу переходим к следующему элементу
                if len(s) != len(word):
                    continue
                else:
                    # Определяем count - сколько раз элементы разные.
                    count = 0
                    # Итерируем по слову, смотрим сколько несовпадений
                    for i in range(len(s)):
                        if s[i] != word[i]:
                            count += 1

                    # Если несовпадение одно по итогу - возвращаем True.
                    if count == 1:
                        return True

            return False



obj = MagicDictionary()
obj.buildDict(["hello","hallo","leetcode","judge"])
print(obj.search("judge"))

# O(N*M), где N - кол-во слов в строке, M - количество символов в строках
# O(N)

import collections

### Solution from LEETCODE
class MagicDictionary2(object):
    def __init__(self):
        # Создаем дефолт дикт, у которого пустой лист по умолчанию в качестве ключа
        self.buckets = collections.defaultdict(list)

    def buildDict(self, words):
        # Добавляем в словарь по ключу(длина слова), (value-лист)  -- слова.
        for word in words:
            self.buckets[len(word)].append(word)

    def search(self, word):
        # Т.к. у нас по ключу уже рассортировано значение, то:
        # 1. Смотрим по каждому кандидату, длина которого равна входному слову (если длина не найдена, вернется пустой лист, т.к. он дефолтный)
        return any(sum(a!=b for a,b in zip(word, candidate)) == 1
                   for candidate in self.buckets[len(word)])



### Solution from LEETCODE 2. Альтернативное решение.
class MagicDictionary3(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        # По умолчанию сет как ключ
        self.dmap = collections.defaultdict(set)


    #Time Complexity: O(sum(w)) где w - длина слова.
    def buildDict(self, dict):
        """
        Build a dictionary through a list of words
        :type dict: List[str]
        :rtype: void
        """
        # Идем по слову, и формируем из него маски. Apple - *pple, A*ple и т.д. И добавляем все их как ключ в словарь (где значение это пропущенная буква).
        for word in dict:
            for x in range(len(word)):
                key = word[:x] + "*" + word[x+1:]
                self.dmap[key].add(word[x])

    #O(K^2) space when generating neighbors to search. K is the length of our search word.
    def search(self, word):
        """
        Returns if there is any word in the trie that equals to the given word after modifying exactly one character
        :type word: str
        :rtype: bool
        """
        # Создаем маски для входного слова. Убираем один символ по очереди.
        for x in range(len(word)):
            key = word[:x] + "*" + word[x+1:]
            # Смотрим что отдает по нашей маске, какую букву.
            values = self.dmap[key]
            # Если значений для этой маски нет, значит убрать один символ недостаточно, или это не тот символ! значит переходим к след элементу, нужно убрать другой.
            if not values: continue
            # Если буквы слова нет в значениях при совпадающей маске, значит это то что надо, 1 симввол изменен. По второму условию не пойму....
            if word[x] not in values or len(values) > 1:
                return True
        return False


obj = MagicDictionary3()
obj.buildDict(["hello"])
print(obj.search("hohllo"))

# Space O(K^2) We use O(K^2) space when generating neighbors to search. K is the length of our search word.