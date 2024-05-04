class Solution(object):
    def checkInclusion(self, s1, s2):
        set1 = dict()
        for ele in s1:
            if ele in set1:
                set1[ele] += 1
            else:
                set1[ele] = 1
        
        if len(s1) > len(s2):
            return False

        set2 = dict()
        for i in range(len(s1)):
            if s2[i] in set2:
                set2[s2[i]] += 1
            else:
                set2[s2[i]] = 1
        for i in range(len(s1), len(s2)):
            if set1 == set2:
                return True
            else:
                set2[s2[i-len(s1)]] -= 1
                if set2[s2[i-len(s1)]] == 0:
                    set2.pop(s2[i-len(s1)])
                if s2[i] in set2:
                    set2[s2[i]] += 1
                else:
                    set2[s2[i]] = 1
        if set1 == set2:
            return True
        return False