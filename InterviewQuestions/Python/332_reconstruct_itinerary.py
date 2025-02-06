# https://leetcode.com/problems/reconstruct-itinerary/description/
from collections import defaultdict, List
from typing import List

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        a = defaultdict(list)

        for ticket in tickets:
            f, t = ticket
            a[f].append(t)
        
        first = "JFK"
        result = []
        def dfs(node):
            while a[node]:
                index = 0
                if len(a[node]) > 1:
                    lowestVal = "ZZZ"
                    for i, val in enumerate(a[node]):
                        if val < lowestVal:
                            lowestVal = val
                            index = i
                nextNode = a[node].pop(index)
                dfs(nextNode)
                result.append(nextNode)
        
        dfs(first)

        

        result.append(first)

        return result[::-1]