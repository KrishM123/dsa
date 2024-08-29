class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    count += 1
                    to_explore = [(i, j)]
                    while to_explore:
                        (curr_i, curr_j) = to_explore.pop()
                        if curr_i >= 0 and curr_i < len(grid) and curr_j >= 0 and curr_j < len(grid[0]) and grid[curr_i][curr_j] == '1':
                            grid[curr_i][curr_j] = '0'
                            to_explore += [(curr_i+1, curr_j), (curr_i-1, curr_j), (curr_i, curr_j+1), (curr_i, curr_j-1)]
        return count
