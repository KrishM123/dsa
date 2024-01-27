class Solution(object):
    def containsDuplicate(self, nums):
        if (min(nums) > 0):
            length = (abs(max(nums))) + 1
        elif (max(nums) < 0):
            length = (abs(min(nums))) + 1
        else:
            length = abs(max(nums)) + abs(min(nums)) + 1
        
        if (length < 500000000):
            freq = [0] * length
            for num in nums:
                freq[num] += 1
                if freq[num] == 2:
                    return True
            return False
        else:
            all_nums = []
            for num in nums:
                if num not in all_nums:
                    all_nums.append(num)
                else:
                    return True
            return False