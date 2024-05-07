#include <iostream>
#include <map>
#include <utility>

using namespace std;

class Solution {
public:
    bool exist(vector<vector<char>>& board, string word) {
        vector<pair<int, int>> taken;
        bool found = false;
        for (int y = 0; y < size(board); y++) {
            for (int x = 0; x < size(board[0]); x++) {
                if (!found && board[y][x] == word[0]){
                    found = helper(board, y, x, word, 1, taken);
                }
            }
        }
        return found;
    }

    bool helper(vector<vector<char>>& board, int curr_y, int curr_x, string& word, int word_pos, vector<pair<int, int>> taken) {

        if (word_pos == size(word)) {
            return true;
        }
        taken.push_back(make_pair(curr_x, curr_y));
        bool found = false;
        if (!found && curr_y+1 < size(board) && board[curr_y+1][curr_x] == word[word_pos] && find(taken.begin(), taken.end(), make_pair(curr_x, curr_y+1)) == taken.end()) {
            found = helper(board, curr_y+1, curr_x, word, word_pos + 1, taken);
        }
        if (!found && curr_y-1 >= 0 && board[curr_y-1][curr_x] == word[word_pos] && find(taken.begin(), taken.end(), make_pair(curr_x, curr_y-1)) == taken.end()) {
            found = helper(board, curr_y-1, curr_x, word, word_pos + 1, taken);
        }
        if (!found && curr_x+1 < size(board[0]) && board[curr_y][curr_x+1] == word[word_pos] && find(taken.begin(), taken.end(), make_pair(curr_x+1, curr_y)) == taken.end()) {
            found = helper(board, curr_y, curr_x+1, word, word_pos + 1, taken);
        }
        if (!found && curr_x-1 >= 0 && board[curr_y][curr_x-1] == word[word_pos] && find(taken.begin(), taken.end(), make_pair(curr_x-1, curr_y)) == taken.end()) {
            found = helper(board, curr_y, curr_x-1, word, word_pos + 1, taken);
        }
        return found;
    }
};