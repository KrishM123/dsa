class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_pos = 0
        for pos in range(len(nums) - 1):
            max_pos = max(max_pos, pos + nums[pos])
            if nums[pos] == 0 and max_pos <= pos:
                return False
        return True