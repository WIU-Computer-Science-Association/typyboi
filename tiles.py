from typyboi import items, enemies

class World:
    def __init__(self, json_file = None):
        self.map = {}

    def add_tile(self, tile):
        self.map[(tile.x, tile.y)] = tile

    def get_adjacent_tiles(self, x, y):
        adjacent_tiles = []
        # Check north
        if((x, y + 1) in self.map):
            adjacent_tiles.append(self.map[(x, y + 1)])
        # Check east
        if((x + 1, y) in self.map):
            adjacent_tiles.append(self.map[(x + 1, y)])
        #Check south
        if((x, y - 1) in self.map):
            adjacent_tiles.append(self.map[(x, y - 1)])
        #Check west
        if((x - 1, y) in self.map):
            adjacent_tiles.append(self.map[(x - 1, y)])

        return adjacent_tiles

 
class MapTile:
    def __init__(self, x, y, flavor_text = ''):
        self.x = x
        self.y = y
        self.flavor_text = flavor_text
 
    def modify_player(self, player):
        pass

class LootRoom(MapTile):
    def __init__(self, x, y, item_list = [], gold = 0):
        self.item_list = item_list
        self.gold = gold
        super().__init__(x, y)
 
    def add_loot(self, player):
        player.inventory.append(self.item_list)
        player.inventory.add_gold(self.gold)
        self.item_list = []
        self.gold = 0
 
    def modify_player(self, player):
        self.add_loot(player)

class EnemyRoom(MapTile):
    def __init__(self, x, y, enemy):
        self.enemy = enemy
        super().__init__(x, y)
 
    def modify_player(self, the_player):
        if self.enemy.is_alive():
            the_player.hp = the_player.hp - self.enemy.damage
            print("Enemy does {} damage. You have {} HP remaining.".format(self.enemy.damage, the_player.hp))

 