class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        for pos1 in range(len(nums)):
            for pos2 in range(pos1 + 1, len(nums)):
                if nums[pos1] + nums[pos2] == target:
                    return [pos1, pos2]