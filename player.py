from typyboi import items
 
class Player:
    def __init__(self, x, y):
        self.inventory = Inventory()
        self.hp = 100
        self.location_x = x
        self.location_y = y
        self.victory = False
 
    def is_alive(self):
        return self.hp > 0
 
    def print_inventory(self):
        for item in self.inventory.items:
            print(item, '\n')
        print('gold: ' + self.inventory.gold, '\n')
    
    def move(self, dx, dy):
        self.location_x += dx
        self.location_y += dy  
 
    def move_north(self):
        self.move(dx=0, dy=-1)
    
    def move_south(self):
        self.move(dx=0, dy=1)
    
    def move_east(self):
        self.move(dx=1, dy=0)
    
    def move_west(self):
        self.move(dx=-1, dy=0)

class Inventory():
    def __init__(self, items = [], gold = 0):
        self.items = items
        self.gold = gold
    
    def add_item(self, item):
        self.items.append(item)

    def add_gold(self, gold):
        self.gold += gold