from typyboi import items, enemies
 
class MapTile:
    def __init__(self, x, y, flavor_text = ''):
        self.x = x
        self.y = y
        self.flavor_text = flavor_text
 
    def modify_player(self, player):
        pass

class StartingRoom(MapTile):
    def __init__(self, x, y, flavor_text):
        super().__init__(x, y, flavor_text)
 
    def modify_player(self, player):
        #Room has no action on player
        pass

class LootRoom(MapTile):
    def __init__(self, x, y, item_list = [], gold = 0):
        self.item_list = item_list
        self.gold = gold
        super().__init__(x, y)
 
    def add_loot(self, player):
        player.inventory.append(self.item_list)
        player.inventory.add_gold(self.gold)
 
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

class EmptyCavePath(MapTile):

    def modify_player(self, player):
        #Room has no action on player
        pass
 