class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        start = 0
        end = (m  * n) - 1

        while start <= end:
            mid = (start + end) // 2
            if matrix[mid // n][mid % n] < target:
                start = mid + 1
            elif matrix[mid // n][mid % n] > target:
                end = mid - 1
            else:
                return True
        return False


        # m = len(matrix) - 1
        # n = len(matrix[0])
        # start = [0, 0]
        # end = [m, n - 1]
        # middle = [int(((((start[0] * n) + start[1]) + ((end[0] * n) + end[1])) / 2) / n), int((((start[0] * n) + start[1]) + ((end[0] * n) + end[1])) / 2) % n]

            
        # if (matrix[start[0]][start[1]] == target or matrix[end[0]][end[1]] == target):
        #     return True
        # while ((start[0] * n) + start[1]) + 1 < ((end[0] * n) + end[1]):            
        #     if (matrix[start[0]][start[1]] == target or matrix[end[0]][end[1]] == target):
        #         return True
        #     if matrix[middle[0]][middle[1]] > target:
        #         end = middle
        #         middle = [int(((((start[0] * n) + start[1]) + ((end[0] * n) + end[1])) / 2) / n), int((((start[0] * n) + start[1]) + ((end[0] * n) + end[1])) / 2) % n]
        #     elif matrix[middle[0]][middle[1]] < target:
        #         start = middle
        #         middle = [int(((((start[0] * n) + start[1]) + ((end[0] * n) + end[1])) / 2) / n), int((((start[0] * n) + start[1]) + ((end[0] * n) + end[1])) / 2) % n]
        #     else:
        #         return True
        # return False