class Solution:
    def earliestAcq(self, logs: List[List[int]], n: int) -> int:
        
        logs = sorted(logs, key = lambda x:x[0])
        print(logs)
        
        graph = collections.defaultdict(set)
        print(graph)
        
        for i in range(n):
            graph[i] = {i}
            
        for ts, n1, n2 in logs:
            graph[n1] = graph[n1].union(graph[n2])
            
            # print(graph)
            for x in graph[n1]:
                graph[x] = graph[n1]
            
            if len(graph[n1]) == n:
                return ts
        
        return -1