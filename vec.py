class Vec:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def __add__(self,a):
        return Vec(self.x + a.x, self.y + a.y)

    def __repr__(self):
        return "(%d,%d)" % (self.x, self.y)
