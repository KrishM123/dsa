class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        people_that_dont_trust = set()
        people_trusting_you = {}

        for num in range(1, n + 1):
            people_that_dont_trust.add(num)
            people_trusting_you[num] = []

        for relationship in trust:
            [truster, trustee] = relationship
            if truster in people_that_dont_trust:
                people_that_dont_trust.remove(truster)
            
            people_trusting_you[trustee].append(truster)

        for person in people_that_dont_trust:
            if len(people_trusting_you[person]) == n-1:
                return person
        return -1  