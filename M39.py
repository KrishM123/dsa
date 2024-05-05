import copy

class Solution(object):
    def combinationSum(self, candidates, target):
        self.curr_combinations = []
        for pos in range(len(candidates)):
            if candidates[pos] <= target:
                self.helper(candidates[pos:], target, [candidates[pos]])
        return self.curr_combinations
        
    def helper(self, candidates, target, sum_list):
        curr_sum = sum(sum_list)
        if curr_sum == target:
            self.curr_combinations.append(sum_list)
        else:
            for pos in range(len(candidates)):
                if candidates[pos] + curr_sum <= target:
                    new_list = copy.copy(sum_list)
                    new_list.append(candidates[pos])
                    self.helper(candidates[pos:], target, new_list)