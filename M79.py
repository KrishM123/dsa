import copy

class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        found = False
        taken = set()
        for i in range(len(board)):
            for j in range(len(board[0])):
                if not found and board[i][j] == word[0]:
                    new_taken = copy.copy(taken)
                    found = self.helper(board, word, i, j, 1, new_taken)
        return found

    def helper(self, board, word, i, j, word_pos, taken):
        if word_pos >= len(word):
            return True
            
        taken.add((i, j))

        found = False
        if not found and (i+1, j) not in taken and i + 1 < len(board) and board[i+1][j] == word[word_pos]:
            new_taken = copy.copy(taken)
            found = self.helper(board, word, i+1, j, word_pos + 1, new_taken)
        if not found and (i, j+1) not in taken and j + 1 < len(board[0]) and board[i][j+1] == word[word_pos]:
            new_taken = copy.copy(taken)
            found = self.helper(board, word, i, j+1, word_pos + 1, new_taken)
        if not found and (i-1, j) not in taken and i - 1 >= 0 and board[i-1][j] == word[word_pos]:
            new_taken = copy.copy(taken)
            found = self.helper(board, word, i-1, j, word_pos + 1, new_taken)
        if not found and (i, j-1) not in taken and j - 1 >= 0 and board[i][j-1] == word[word_pos]:
            new_taken = copy.copy(taken)
            found = self.helper(board, word, i, j-1, word_pos + 1, new_taken)
        return found