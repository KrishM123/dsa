class Solution(object):
    def isValid(self, s):
        opening = ['(', '{', '[']
        partner = {
            '(': ')',
            '{': '}',
            '[': ']'
        }
        stack = []
        for pos in range(len(s)):
            if s[pos] in opening:
                stack.append(s[pos])
            elif len(stack) > 0:
                if s[pos] != partner[stack[-1]]:
                    return False
                else:
                    stack = stack[:-1]
            else:
                return False
        if len(stack) != 0:
            return False
        return True