class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        #method k is suspicious, and anything k calls (directly or through a chain) is suspicious too
        #build a graph of who invokes who, then dfs out from k to flag every suspicious method
        #but we can only remove them if no clean method depends on a suspicious one
        #so scan the invocations, if a non suspicious method calls a suspicious one, removing is unsafe
        #if its safe, return only the clean methods, otherwise return every method untouched

        #adjacency list of each method to the methods it invokes
        graph = [[] for _ in range(n)]
        for a, b in invocations:
            graph[a].append(b)

        #mark every method reachable from k as suspicious
        suspicious = [False] * n

        def dfs(node):
            suspicious[node] = True
            for nxt in graph[node]:
                if not suspicious[nxt]:
                    dfs(nxt)

        dfs(k)

        #if a clean method invokes a suspicious one, we cant safely remove anything
        for a, b in invocations:
            if not suspicious[a] and suspicious[b]:
                return [i for i in range(n)]

        #safe to remove, so hand back only the methods that arent suspicious
        return [i for i in range(n) if not suspicious[i]]
