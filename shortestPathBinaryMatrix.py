class Solution(object):
    def shortestPathBinaryMatrix(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        def is_valid(x,y): 
            return -1 < x < len(grid) and -1 < y < len(grid[0]) and grid[x][y] == 0

        if grid[0][0] == 1 or grid[-1][-1] == 1: return -1 

        queue = deque()
        queue.append((0,0,1)) 
        grid[0][0] = 1 
        neighbors = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]

        while queue: 
            x,y,cost   = queue.popleft()
            if x == len(grid)-1 and y == len(grid[0])-1: return cost
            for dx,dy in neighbors: 
                new_x, new_y = dx+x,dy+y
                if is_valid(new_x, new_y):
                    grid[new_x][new_y] = 1 
                    queue.append((new_x,new_y,cost+1))
        return -1
