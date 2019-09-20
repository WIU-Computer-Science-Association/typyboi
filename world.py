
_world = {}

def register_world(world = {}):
    '''
        World should be a map with keys (x,y) and 
        values of type MapTile
    '''
    _world = world

def load_world(json_file):
    pass

def add_tile(tile):
    _world[tile.x, tile.y] = tile

def tile_exists(x, y):
    return (x, y) in _world

def get_tile(x, y):
    return _world[(x, y)]
