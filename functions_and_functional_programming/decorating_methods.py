class IslandMaker:
    def __init__(self, suffix):
        self.suffix = suffix


    @tracer
    def make_island(self, name):
        return name + self.suffix

im = IslandMaker(' Island')
im.make_island('Python')
