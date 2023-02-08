class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        graph = collections.defaultdict(set)
        for i in range(len(equations)):
            v1,v2 = equations[i]
            graph[v1].add((v2,values[i]))
            graph[v2].add((v1,1/values[i]))
        
        def dfs(var1, var2, value, visited):
            if var1 == var2:
                res.append(value)
                return True
            if var1 in visited:return False
            visited.add(var1)
            for neighbor,val in graph[var1]:
                if dfs(neighbor, var2, value * val, visited):
                    return True
            return False
        
        res = []
        for v1, v2 in queries:
            if v1 not in graph or v2 not in graph: res.append(-1)
            else:
                is_found = dfs(v1, v2, 1, set())
                if not is_found: res.append(-1)
        
        return res
