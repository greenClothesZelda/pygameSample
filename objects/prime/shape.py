class Shape:
    def __init__(self, x:float, y:float, color:tuple=(0, 0, 0)):
        self.x = x
        self.y = y
        self.color = color

    def draw(self, surface):
        raise NotImplementedError("shape is just a base class")