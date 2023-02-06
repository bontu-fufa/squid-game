class Solution(object):
    def racecar(self, target):
        """
        :type target: int
        :rtype: int
        """
        queue = [[0,1]]
        level = 0
        while len(queue)>0:
            size = len(queue)
            for i in range(size):
                position,speed = queue.pop(0)
                if target==position: return level
                queue.append([position+speed,speed*2])
                current_speed = -1 if speed > 0 else 1
                if (position + speed > target and speed > 0) or (position + speed < target and speed < 0):
                    queue.append([position,current_speed])
            level+=1
