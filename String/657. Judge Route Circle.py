class Solution:
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        u_cnt = moves.count('U')
        d_cnt = moves.count('D')
        l_cnt = moves.count('L')
        r_cnt = moves.count('R')

        if u_cnt == d_cnt and l_cnt == r_cnt:
            return True
        else:
            return False

    def judgeCircle(self, moves):       # Initially, the robot is at (x, y) = (0, 0). If the move is 'U', the robot goes to (x, y-1); if the move is 'R', the robot goes to (x, y) = (x+1, y), and so on.
        x = y = 0
        for move in moves:
            if move == 'U': y -= 1
            elif move == 'D': y += 1
            elif move == 'L': x -= 1
            elif move == 'R': x += 1

        return x == y == 0


sol = Solution()



# O(N), O(1). Where N is the length of moves. We count through the string.
#