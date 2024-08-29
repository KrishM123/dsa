class KthLargest(object):

    def __init__(self, k, nums):
        self.k = k
        self.ints = self.sort_ints(nums)

    def sort_ints(self, nums):
        if len(nums) > 1:
            new_nums = []
            sorted_1 = self.sort_ints(nums[:len(nums) // 2])
            sorted_2 = self.sort_ints(nums[len(nums) // 2:])
            for rep in range(0, len(nums)):
                if len(sorted_1) > 0 and len(sorted_2) > 0 and sorted_1[0] < sorted_2[0]:
                    new_nums.append(sorted_1[0])
                    sorted_1 = sorted_1[1:]
                elif len(sorted_1) > 0 and len(sorted_2) > 0 and sorted_1[0] >= sorted_2[0]:
                    new_nums.append(sorted_2[0])
                    sorted_2 = sorted_2[1:]
                elif len(sorted_1) > 0:
                    new_nums += sorted_1
                    break
                else:
                    new_nums += sorted_2
                    break
            return new_nums
        else:
            return nums

    def add(self, val):
        if len(self.ints) == 0 or val >= self.ints[-1]:
            self.ints.append(val)
        else:
            for pos in range(len(self.ints)):
                if self.ints[pos] > val:
                    self.ints = self.ints[:pos] + [val] + self.ints[pos:]
                    break
        return self.ints[len(self.ints)-self.k]

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)