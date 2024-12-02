class Character:
    def __init__(self,name,hp,Attack,Defense):
        self.name=name
        self.hp =hp
        self.Attack=Attack
        self.Defense=Defense

    def take_damage(self,damage):
        real_damage = max(0,abs(self.Defense-damage))
        self.hp = max(0,self.hp - real_damage)
        return real_damage
    
    def __str__(self):
        return (f"{self.name}, HP: {self.hp}, 공격력: {self.attack}" f"방어력 : {self.Defense}")

        
    def is_alive(self):
        return self.hp > 0


class Hero(Character):
    def __init__(self,name,hp,Attack,Defense,Role):
        super().__init__(name,hp,Attack,Defense)
        self.Role = Role
        self.exp = 0

    def gain_exp(self,amount):
        self.exp += amount

    def special_attack(self):
        if self.Role == "전사":
            return self.Attack + 4
        elif self.Role == "마법사":
            return self.Attack + 3
        elif self.Role == "궁수":
            return self.Attack + 2
        else:
            return self.Attack 
        
    def __str__(self):
        return (f"{self.name}[{self.Role}], HP: {self.hp}, 공격력: {self.attack}" f"방어력 : {self.Defense}, 경험치: {self.exp}")
    
class Monster(Character):
    def __init__(self,name,hp,Attack,Defense):
        super().__init__(name,hp,Attack,Defense)
