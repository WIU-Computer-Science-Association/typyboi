class Enemy:
    def __init__(self, name, hp, damage, gold = 0, items = []):
        self.name = name
        self.hp = hp
        self.damage = damage
        self.gold = gold
        self.items = items
 
    def is_alive(self):
        return self.hp > 0

    def drop_items(self):
        return self.gold, self.items