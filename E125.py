class Solution(object):
    def isPalindrome(self, s):
        pos1 = 0
        pos2 = len(s) - 1
        while (pos1 != pos2 and pos1 <= pos2):
            if (not s[pos1].isalnum()):
                pos1 += 1
            elif(not s[pos2].isalnum()):
                pos2 -= 1
            elif(s[pos1].lower() != s[pos2].lower()):
                return False
            else:
                pos1 += 1
                pos2 -= 1
        return True
        