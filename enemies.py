class Enemy:
    def __init__(self, name, hp, damage, gold = 0, itens = []):
        self.name = name
        self.hp = hp
        self.damage = damage
        self.gold = gold
        self.itens = itens
 
    def is_alive(self):
        return self.hp > 0

    def drop_itens(self):
        return self.gold, self.itens