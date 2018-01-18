class Solution:
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if not board:
            return False
        if not board[0]:
            return False
        if len(word) > len(board) * len(board[0]):
            return False

        def exist_helper(board, word, used, pos):
            if len(word) == 0:
                return True
            if pos[0] >= len(board) or pos[1] >= len(board[0]) or pos[0] < 0 or pos[1] < 0:
                return False
            if word[0] != board[pos[0]][pos[1]]:
                return False
            if len(word) == 1:
                return True

            up = (pos[0] - 1, pos[1])
            down = (pos[0] + 1, pos[1])
            left = (pos[0], pos[1] - 1)
            right = (pos[0], pos[1] + 1)
            used.add(pos)

            res = False
            if left not in used:
                res = res or exist_helper(board,word[1:], used.copy(), left)
            if right not in used:
                res = res or exist_helper(board, word[1:], used.copy(), right)
            if up not in used:
                res = res or exist_helper(board, word[1:], used.copy(), up)
            if down not in used:
                res = res or exist_helper(board,word[1:], used.copy(), down)

            return res

        for i in range(len(board)):
            for j in range(len(board[0])):
                if word[0] == board[i][j]:
                    used = set()
                    flag = exist_helper(board,word, used, (i,j))
                    if flag: return True
        return False

b = [["A","B","C","E"],["S","F","E","S"],["A","D","E","E"]]


s = Solution()
print(s.exist(b, "ABCESEEEFS"))


