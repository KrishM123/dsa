class Solution(object):
    def subarraysDivByK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        prefix_sum = 0
        count = 0
        mod_count = {0: 1}
        for val in nums:
            prefix_sum += val
            prefix_sum %= k
            count += mod_count.get(prefix_sum, 0)            
            mod_count[prefix_sum] = mod_count.get(prefix_sum, 0) + 1
        return count