class Solution(object):
    def restoreArray(self, adjacentPairs):
        """
        :type adjacentPairs: List[List[int]]
        :rtype: List[int]
        """
        graph = collections.defaultdict(set)
        for v1,v2 in adjacentPairs:
            graph[v1].add(v2)
            graph[v2].add(v1)

        start_num = None
        for v,e in graph.items(): 
            if len(e) == 1: 
                start_num = v
                break
                
        original_array = []
        visited = set()

        def dfs(i):
            original_array.append(i)
            visited.add(i)
            for nei in graph[i]:
                if nei not in visited: 
                    dfs(nei)

        dfs(start_num)
        return original_array
