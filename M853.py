class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [[p, s] for p, s in zip(position, speed)]
        sort = sorted(pair)[::-1]
        fleets = 0
        pos1 = 0
        while pos1 < len(sort):
            pos2 = pos1 + 1
            while (pos2 < len(sort)) and sort[pos1][1] != sort[pos2][1] and ((sort[pos2][0] - sort[pos1][0]) / (sort[pos1][1] - sort[pos2][1])) > 0 and ((sort[pos1][1] * ((sort[pos2][0] - sort[pos1][0]) / (sort[pos1][1] - sort[pos2][1]))) + sort[pos1][0] <= target):
                pos2 += 1
            fleets += 1
            pos1 = pos2
        return fleets
