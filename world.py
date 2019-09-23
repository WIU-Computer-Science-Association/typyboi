
class World():
    """Object representation of the game world"""
    def __init__(self):
        """Instantiate the world"""
        self.world = {}

    def add_tile(self, tile):
        """
        Add a new tile to the world
        raise ValueError if a tile already exists at the new tiles
        Keyword arguments:
        tile -- MapTile to add
        """
        x = tile.x
        y = tile.y
        if self.tile_exists(x, y):
            raise ValueError('A tile already exists at ({}, {})'.format(x, y))

        self.world[(x, y)] = tile

    def tile_exists(self, x, y):
        """Check if there is already a tile at these coordinates"""
        return (x, y) in self.world

    def get_tile(self, x, y):
        """
        Return tile at coordinates (x, y)
        Keyword arguments:
        x -- integer x coordinate
        y -- integer y coordinate
        """
        return self.world[(x, y)]
