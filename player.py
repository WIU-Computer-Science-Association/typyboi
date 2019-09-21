from typyboi import items
import random
 
class Player:
    def __init__(self, x, y, max_hp, weapon = items.Weapon('Rock', 'A hard rock', 1, 1)):
        self.inventory = Inventory()
        self.max_hp = max_hp
        self.hp = max_hp
        self.location_x = x
        self.location_y = y
        self.victory = False
        self.equipped_weapon = weapon
        self.moved = True
        if weapon != None:
            self.inventory.add_item(weapon)
 
    def is_alive(self):
        return self.hp > 0

    def add_hp(self, delta_hp):
        new_hp = self.hp + delta_hp
        self.hp = new_hp if new_hp <= self.max_hp else self.max_hp
 
    def print_inventory(self):
        print('Inventory:')
        for item in self.inventory.items:
            print(item, '\n')
        print('gold: ' + str(self.inventory.gold), '\n')
    
    def move(self, dx, dy):
        self.moved = True
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

    def attack(self, enemy):
        self.moved = True
        enemy.hp -= self.equipped_weapon.damage

    def equip_weapon(self):
        weapon_list = self.inventory.get_weapon_list()

        if len(weapon_list) == 0:
            print('You have no weapons')
            return
        else:
            index = 1
            for weapon in weapon_list:
                print(str(index) + ': ' + weapon.__str__(), '\n')
            print('q: quit', '\n')
            choice = input('Choose a weapon: ')
            if choice == 'q':
                return
            
            try:
                selected_index = int(choice) - 1
                if 0 <= selected_index < len(weapon_list):
                    selected_weapon = weapon_list[selected_index]
                    self.equipped_weapon = selected_weapon
                else:
                    raise ValueError('Bad index')
            except ValueError:
                print('Invalid input')   

    def flee(self, tile):
        available_moves = tile.adjacent_moves()
        r = random.randint(0, len(available_moves) - 1)
        self.do_action(available_moves[r])

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
    
    def get_weapon_list(self):
        weapon_list = []
        for item in self.items:
            if isinstance(item, items.Weapon):
                weapon_list.append(item)
        
        return weapon_list