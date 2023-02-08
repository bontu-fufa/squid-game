class Solution(object):
    def numBusesToDestination(self, routes, source, target):
        """
        :type routes: List[List[int]]
        :type source: int
        :type target: int
        :rtype: int
        """
        if source == target: return 0
        graph = defaultdict(list)

        for i in range(len(routes)):
            for stop in routes[i]: graph[stop].append(i)

        if target not in graph: return -1

        visited = set(graph[source])
        queue = deque(graph[source])
        res = 0

        while queue:
            size = len(queue)
            res += 1
            for _ in range(size):
                route = queue.popleft()
                for stop in routes[route]:
                    if stop == target: return res
                    for i in graph[stop]:
                        if i in visited: continue
                        queue.append(i)
                        visited.add(i)
        return -1
