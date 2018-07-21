# -*- coding: utf-8 -*-

from collections import deque

class Solution:
    def generateParenthesis(self, n):
        res_list = []

        # Передаем лист, количество левых и правых скобок, n, и строку для формирования промежуточного результата.
        self.helper_dfs(res_list, 0, 0, n, '')
        return res_list


    # Функция обертка, принимает параметры. Функция изменяет лист.
    # По сути поиск в глубину, DFS. Проходим вглубь каждой ветви до достижения результата. Затем по стеку возвращаемся вверх, и идем в другие ветки.
    def helper_dfs(self, res_list, l, r, n, res_s):

        # Возвращаемся только тогда, когда достигнем листов. Т.е. оба варианта левых и правых скобок будут закончены.
        if l == n and r == n:
            res_list.append(res_s)
            return

        # Если левые скобки еще остались, т.е. они меньше n, значит добавляем открытую.
        if l < n:
            self.helper_dfs(res_list, l+1, r, n, res_s + '(')

        # Дальше еще вариант, если кол-во правых скобок меньше левых, тогда добавляем и правую.
        if r < l:
            self.helper_dfs(res_list, l, r+1, n, res_s + ')')


    # Метод 2. Вызывать напрямую.
    # Используем BFS. Смотрим соседей сразу, через очередь. И смотрим всех соседей пока не достигнем дна.
    def helper_bfs(self, n):

        res_list = []
        q = deque()

        # Создаем экземпляр класса, скармливаем ему пустую строку, и нули как количество скобок. И добавляем его в очередь.
        node = Node('', 0, 0)
        q.appendleft(node)

        while q:
            # Забираем из очереди ноду
            node = q.pop()

            # Если левая и правая достигли "дна", то есть нижнего уровня, тогда добавляем значение ноды(строку) в результирующий лист.
            if node.left == n and node.right == n:
                res_list.append(node.s)

            # Если количество левых скобок меньше n, добавляем их. И ноду в очередь.
            if node.left < n:
                q.appendleft(Node(node.s + '(', node.left + 1, node.right))

            # Если количество правых скобок меньше меньше левых, добавляем их. И ноду в очередь.
            if node.right < node.left:
                q.appendleft(Node(node.s + ')', node.left, node.right + 1))

        return res_list



# Вспомогательный класс, который будет содержать информацию о текущем количестве скобок, и результирующую строку.
class Node:
    def __init__(self, s, left, right):
        self.s = s
        self.left = left
        self.right = right





# Решение на ютубе. https://www.youtube.com/watch?v=JKXs7a4RMFU
# Сложность НЕ 2^n, как можно подумать, а 4^n/sqrt(n). Некий Catalan number.
#Complexity Analysis
#https://leetcode.com/articles/generate-parentheses/

sol = Solution()


print(sol.helper_bfs(3))



