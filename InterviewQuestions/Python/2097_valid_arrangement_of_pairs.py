# https://leetcode.com/problems/valid-arrangement-of-pairs/description/

from collections import defaultdict
class Solution:
    def validArrangement(self, pairs: list[list[int]]) -> list[list[int]]:
        # find the first one on the graph, with it being in
        result = []
        graph = defaultdict(list)
        inOut = defaultdict(int)

        for a, b in pairs:
            graph[a].append(b)
            inOut[a] += 1
            inOut[b] -= 1
        
        start = -1
        for key, val in inOut.items():
            if val == 1:
                start = key
                break

        if start == -1:
            start = pairs[0][0]

        def dfs(node):
            while graph[node]:
                nextNode = graph[node].pop()
                dfs(nextNode)
                result.append([node, nextNode])

        dfs(start)

        return result[::-1]