
class World():
    
    def __init__(self):
        self.world = {}

    def add_tile(self, tile):
        self.world[(tile.x, tile.y)] = tile

    def tile_exists(self, x, y):
        return (x, y) in self.world

    def get_tile(self, x, y):
        return self.world[(x, y)]
