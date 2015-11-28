class Field:
    def __init__(self, width, height):
        self.width   = width
        self.height  = height
        self.borders = {}
        self.objects = {}

    def add_robot(self, name, pos):
        if name in self.objects:
            return None
        return self.objects[name] = Robot(pos, name)

    def move(self, obj, side):
        if self.is_bord(obj, side):
            self.destroy(obj)
        obj.pos += side.vec()

    def is_bord(self, obj, side):
        return __check_bord(obj.pos, obj.pos + side.vec())

    def __check_bord(a,b):
        if (a,b) in self.borders or (b,a) in self.borders:
            return True
        else:
            return False

    def mark(self,)

class Robot:
    def __init__(self, pos, name = None):
        self.name = name
        self.pos  = pos

    # def move(self, side):
    #     old_pos = self.pos
    #     self.pos += side.vec()
    #     if
    #     if (self.pos, old_pos) in self.borders:
    #         self.destroy()
    #         return
    #     if (old_pos, self.pos) in self.borders:
    #         self.destroy()
    #
    # def is_bord(self, side):
