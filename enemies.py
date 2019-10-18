class Enemy:
    def __init__(self, name, hp, damage, accuracy, gold = 0, items = []):
        """
        Keyword arguments:
        name        -- string name of the enemy
        hp          -- int health value
        damage      -- int damage value
        accuracy    -- int for accuracy %, max 100
        gold        -- int gold dropped
        items       -- list of items dropped
        """
        self.name = name
        self.hp = hp
        self.damage = damage
        self.accuracy = accuracy
        self.gold = gold
        self.items = items
 
    def is_alive(self):
        """Return true if the enemies hp is greater than 0"""
        return self.hp > 0

    def drop_items(self):
        """Return enemies gold and items as a tupple"""
        return self.gold, self.items
