from typyboi.items import Weapon
from typyboi.items import HealingItem
import random
 
class Player:
    def __init__(self, x, y, max_hp, weapon = Weapon('Rock', 'A hard rock', 2, 1, 90)):
        """
        Instantiate a Player object
        Keyword arguments:
        x       -- integer x coordinate
        y       -- integer y coordinate
        max_hp  -- integer maximum hp for the player
        weapon  -- Weapon equipped to player (default Rock)
        """
        self.inventory = Inventory()
        self.max_hp = max_hp
        self.hp = max_hp
        self.location_x = x
        self.location_y = y
        self.victory = False
        self.equipped_weapon = weapon
        self.moved = True               # Tells if the players last action counts as a move
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
        self.moved = False
    
    def move(self, dx, dy):
        self.moved = True
        self.location_x += dx
        self.location_y += dy  
 
    def move_north(self):
        self.move(dx=0, dy=1)
    
    def move_south(self):
        self.move(dx=0, dy=-1)
    
    def move_east(self):
        self.move(dx=1, dy=0)
    
    def move_west(self):
        self.move(dx=-1, dy=0)

    def attack(self, enemy):
        self.moved = True
        if(random.randint(1,100) > self.equipped_weapon.accuracy):
	        print('Attack missed!')
        else:
                if(self.equip_weapon == None):
                        enemy.hp -= 1
                        return
                enemy.hp -= self.equipped_weapon.damage
        #print(enemy.hp) #for testing purposes

        if (not enemy.is_alive()):
            self.get_enemy_items(enemy)

    def get_enemy_items(self, enemy):
        dropped_gold, dropped_items = enemy.drop_items()
        self.inventory.add_gold(dropped_gold)
        for item in dropped_items:
            self.inventory.add_item(item)

    def equip_weapon(self):
        weapon_list = self.inventory.get_weapon_list()

        if len(weapon_list) == 0:
            print('You have no weapons')
            return
        else:
            index = 1
            for weapon in weapon_list:
                print(str(index) + ': ' + weapon.__str__(), '\n')
                index += 1
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
        self.moved = False   

    def use_heal_item (self):
        healing_list = self.inventory.get_healing_item_list()

        if len(healing_list) == 0:
            print('You have no heal items')
            return
        else:
            index = 1
            for item in healing_list:
                print(str(index) + ': ' + item.__str__(), '\n')
                index += 1
            print('q: quit', '\n')
            choice = input('Choose a heal item: ')
            if choice == 'q':
                return
            
            try:
                selected_index = int(choice) - 1
                if 0 <= selected_index < len(healing_list):
                    hp = healing_list[selected_index].heal
                    self.add_hp (hp) # use item to add hp to player
                    self.inventory.delete_inventory_item(healing_list[selected_index])
                else:
                    raise ValueError('Bad index')
            except ValueError:
                print('Invalid input')
        self.moved = True   

    def flee(self, tile):
        available_moves = tile.get_adjacent_moves()
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
            if isinstance(item, Weapon):
                weapon_list.append(item)
        
        return weapon_list

    def get_healing_item_list(self):
        healing_list = []
        for item in self.items:
            if isinstance(item, HealingItem):
                healing_list.append(item)

        return healing_list

    def delete_inventory_item (self, usedItem):
        ''' Searches for the first item with same name in inventory to delete'''
        i = 0
        for idx, item in enumerate(self.items):
            if (item.name == usedItem.name):
                i = idx
                break
        self.items.pop(i)
