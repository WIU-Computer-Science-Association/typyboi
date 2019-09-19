from typyboi import items
 
class Player:
    def __init__(self, x, y, max_hp):
        self.inventory = Inventory()
        self.max_hp = max_hp
        self.hp = max_hp
        self.location_x = x
        self.location_y = y
        self.victory = False
 
    def is_alive(self):
        return self.hp > 0

    def add_hp(self, delta_hp):
        new_hp = self.hp + delta_hp
        self.hp = new_hp if new_hp <= self.max_hp else self.max_hp
 
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

    def do_action(self, action, **kwargs):
        action_method = getattr(self, action.method.__name__)
        if action_method:
            action_method(**kwargs)

class Inventory():
    def __init__(self, items = [], gold = 0):
        self.items = items
        self.gold = gold
    
    def add_item(self, item):
        self.items.append(item)

    def add_gold(self, gold):
        self.gold += gold