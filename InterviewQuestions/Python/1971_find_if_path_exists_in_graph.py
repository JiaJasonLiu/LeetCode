# https://leetcode.com/problems/find-if-path-exists-in-graph/description/
# https://www.youtube.com/watch?v=knLFe7hEp3Y

# Mine -> didn't solve all
class Solution:
    
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        if len(edges) == 0:
            return True

        graph = defaultdict(list)
        for i, o in edges:
            graph[i].append(o)
            graph[o].append(i)

        print(graph)
        def dfs(node, des):
            while graph[node]:
                print("node")
                print(node)
                print("graph[node]")
                print(graph[node])
                if des in graph[node]:
                    return True
                nextNode = graph[node].pop()
                graph[nextNode].remove(node)
                return dfs(nextNode, des)

        result = dfs(source, destination)
        if result == None:
            return False
            
        return result

# don't pop -> use a seen set

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        if len(edges) == 0:
            return True

        graph = defaultdict(list)
        for i, o in edges:
            graph[i].append(o)
            graph[o].append(i)

        seen = set()
        def dfs(node, visited):
            if node == destination:
                return True
            seen.add(node)
            for nei_node in graph[node]:
                if nei_node not in visited:
                    if dfs(nei_node, visited):
                        return True
            return False

        result = dfs(source, seen)
        return result