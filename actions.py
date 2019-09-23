from typyboi.player import Player
 
class Action():
    """
        Super class for all actions
    """
    def __init__(self, method, name, hotkey, **kwargs):
        """
        Keyword arguments:
        method -- the action method to perform
        name   -- name of the action
        hotkey -- key that triggers this action
        kwargs -- arguments to pass to the method
        """
        self.method = method
        self.hotkey = hotkey
        self.name = name
        self.kwargs = kwargs
 
    def __str__(self):
        """
        Return a string representation of this action of the form hotkey: name
        """
        return "{}: {}".format(self.hotkey, self.name)

class MoveNorth(Action):
    def __init__(self):
        super().__init__(method=Player.move_north, name='Move north', hotkey='n')
 
class MoveSouth(Action):
    def __init__(self):
        super().__init__(method=Player.move_south, name='Move south', hotkey='s')
 
class MoveEast(Action):
    def __init__(self):
        super().__init__(method=Player.move_east, name='Move east', hotkey='e')
 
class MoveWest(Action):
    def __init__(self):
        super().__init__(method=Player.move_west, name='Move west', hotkey='w')
 
class ViewInventory(Action):
    """Prints the player's inventory"""
    def __init__(self):
        super().__init__(method=Player.print_inventory, name='View inventory', hotkey='i')

class EquipWeapon(Action):
    def __init__(self):
        super().__init__(method=Player.equip_weapon, name='Equip Weapon', hotkey='h')

class Attack(Action):
    def __init__(self, enemy):
        super().__init__(method=Player.attack, name="Attack", hotkey='a', enemy=enemy)

class Flee(Action):
    def __init__(self, tile):
        super().__init__(method=Player.flee, name='Flee', hotkey='f', tile=tile)