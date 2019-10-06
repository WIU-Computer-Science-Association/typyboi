class Item():
    """The base class for all items"""
    def __init__(self, name, description, value):
        """
        Keyword arguments:
        name        -- string name of the item
        description -- string description of the item
        value       -- integer value of the item
        """
        self.name = name
        self.description = description
        self.value = value
 
    def __str__(self):
        return "{}\n=====\n{}\nValue: {}\n".format(self.name, self.description, self.value)

class Weapon(Item):
    """Weapon subclass of item"""
    def __init__(self, name, description, value, damage):
        """
        Keyword arguments:
        name        -- string name of the item
        description -- string description of the item
        value       -- integer value of the item
        damage      -- integer damage for the weapon
        """
        self.damage = damage
        super().__init__(name, description, value)
 
    def __str__(self):
        return "{}\n=====\n{}\nValue: {}\nDamage: {}".format(self.name, self.description, self.value, self.damage)

class HealingItem(Item):
    """Healing Item subclass of item"""
    def __init__(self, name, description, value, heal):
        """
        Keyword arguments:
        name        -- string name of the item
        description -- string description of the item
        value       -- integer value of the item
        heal        -- integer healing power for the item
        """
        self.heal = heal
        super().__init__(name, description, value)
 
    def __str__(self):
        return "{}\n=====\n{}\nValue: {}\nHeal Power: {}".format(self.name, self.description, self.value, self.heal)
