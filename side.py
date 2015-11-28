###from vec import Vec
class Side:
    def __init__(self, side):
        self.side = side

    def __invert__(self):
        return Side({
            'n': 's',
            's': 'n',
            'w': 'e',
            'e': 'w'
        }[self.side])

    def vec(self):
        return {
            'n': Vec( 0,-1),
            's': Vec( 0, 1),
            'w': Vec(-1, 0),
            'e': Vec( 1, 0)
        }[self.side]

    def __repr__(self):
        return "'%s'" % self.side
