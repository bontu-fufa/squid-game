class Solution(object):
    def isRobotBounded(self, instructions):
        """
        :type instructions: str
        :rtype: bool
        """
        
        directions = ([-1, 0], [0, -1], [1, 0], [0, 1])
        start = [0,0]
        x = 0
        for i in range(len(directions)):
            for instruction in instructions:
                if instruction == "G":
                    start[0] += directions[x][0]
                    start[1] += directions[x][1]
                if instruction == "L":
                     x = (x + 1) % 4 
                if instruction == "R": 
                    x = (x - 1) % 4
        return True if start == [0,0] else False 
