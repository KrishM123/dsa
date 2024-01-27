class Solution(object):
    def groupAnagrams(self, strs):
        ref = {}
        for string in strs:
            tot_sum = 0
            tot_prod = 1
            for char in string:
                tot_sum += ord(char)
                tot_prod *= ord(char)
            try: 
                ref[str([tot_sum, tot_prod])].append(string)
            except KeyError:
                ref[str([tot_sum, tot_prod])] = [string]
        to_ret = []
        for key in ref:
            to_ret.append(ref[key])
        return to_ret
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        