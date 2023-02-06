class DetectSquares(object):

    def __init__(self):
        self.points = defaultdict(dict)

    def add(self, point):
        """
        :type point: List[int]
        :rtype: None
        """
        x, y = point
        if y in self.points[x]:
            self.points[x][y] += 1
        else:
            self.points[x][y] = 1

    def count(self, point):
        """
        :type point: List[int]
        :rtype: int
        """
        x, y = point
        res = 0 
        if x in self.points:
            for p in self.points[x]:
                diff = abs(y-p)
                if diff > 0:
                    if x-diff in self.points and y in self.points[x-diff] and p in self.points[x-diff]:
                        res += self.points[x-diff][y] * self.points[x-diff][p] * self.points[x][p] 
                    if x+diff in self.points and y in self.points[x+diff] and p in self.points[x+diff]:
                        res += self.points[x+diff][y] * self.points[x+diff][p] * self.points[x][p] 
        return res 


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)
