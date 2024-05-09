class Solution(object):
    def isPalindrome(self, x):
        return [i for i in str(x)] == [i for i in str(x)][::-1]