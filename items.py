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
    def __init__(self, name, description, value, damage, hit_chance):
        """
        Keyword arguments:
        name        -- string name of the item
        description -- string description of the item
        value       -- integer value of the item
        damage      -- integer damage for the weapon
	hit_chance  -- integer percent of hit chance, max is 100
        """
        self.damage = damage
        self.hit_chance = hit_chance
        super().__init__(name, description, value)
 
    def __str__(self):
        return "{}\n=====\n{}\nValue: {}\nDamage: {}\nAccuracy: {}%".format(self.name, self.description, self.value, self.damage, self.hit_chance)

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
