class Solution(object):
    def search(self, nums, target):
        mid_index = (len(nums)) / 2
        start_index = 0
        end_index = len(nums) - 1
        while (nums[mid_index] != target and start_index < end_index):
            if (((target < nums[mid_index] and (target >= nums[start_index] or nums[start_index] > nums[mid_index]))) or (target > nums[mid_index] and target > nums[end_index] and nums[start_index] > nums[mid_index])):
                end_index = mid_index - 1
            else :
                start_index = mid_index + 1
            mid_index = start_index + ((end_index - start_index) / 2)
        if nums[mid_index] == target:
            return mid_index
        return -1
        