class Solution(object):
    def xorQueries(self, arr, queries):
        """
        :type arr: List[int]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        n = len(arr)
    
        prefix_xor = [0] * (n + 1)
        for i in range(1, n + 1):
            prefix_xor[i] = prefix_xor[i - 1] ^ arr[i - 1]
        
        answer = []
        for query in queries:
            l, r = query
            ans = prefix_xor[r + 1] ^ prefix_xor[l]
            answer.append(ans)
        
        return answer