class UIBlock:
    def __init__(self, x, y):
        self.lst = []
        self.x = x
        self.y = y

    def add(self, obj):
        if not self.lst:
            obj.x = self.x
            obj.y = self.y
        else:
            obj.x = self.x
            obj.y = self.lst[-1].y + self.lst[-1].size
        self.lst.append(obj)

    def draw(self):
        for i in self.lst:
            i.draw()
