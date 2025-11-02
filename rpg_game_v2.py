# Welcome to my first RPG GAME
import random
import time


enemies = [
    ("Goblin", 70),
    ("Orc", 90),
    ("Undead Mage", 50),
    ("Undead Warrior", 120),
    ("Skeleton Archer", 80),
    ("Dark Knight", 150),
    ("Vampire", 130),
    ("Werewolf", 160),
    ("Necromancer", 100),
    ("Demon Imp", 60),
    ("Shadow Assassin", 110),
    ("Fire Elemental", 140),
    ("Ice Golem", 180),
    ("Bandit", 75),
    ("Troll", 200),
    ("Stone Guardian", 250),
    ("Fallen Paladin", 170),
    ("Ghost", 60),
    ("Zombie", 85),
    ("Wraith", 120),
    ("Lich King", 300),
    ("Corrupted Elf", 95),
    ("Blood Sorcerer", 150),
    ("Poison Serpent", 100),
    ("Hellhound", 130),
    ("Minotaur", 220),
    ("Forest Spirit", 80),
    ("Sand Wraith", 115),
    ("Dragon Hatchling", 180),
    ("Ancient Dragon", 400)
]

class Player:
    def __init__(self,name):
        self.name = name

    def attack(self,target):
        print(f"{self.name} attacking {target.name}")

    def damage(self,amount):
        self.health -= amount
        print(f"Player {self.name} is taking {amount} damage , remaining life: {self.health}")
    
    def show_health(self):
        print(f"{self.name} has {self.health} HP")

    def counter_damage(self,amount):
        self.health -= amount
        print(f"Player {self.name} is hit by a magical counterattack! Loses {amount} damage , remaining life: {self.health}")

    def is_dead(self):
        if self.health <= 0:
            return True
        else:
            return False
        

 
class Warrior(Player):
    def __init__(self, name):
        super().__init__(name)
        self.health = 150
        self.armor = 100

    def announce_player(self):
        print(f"Mighty Warrior {self.name} welcome ! You have {self.health}HP and {self.armor}  armor!")

class Mage(Player):
     def __init__(self, name):
        super().__init__(name)
        self.health = 80
        self.armor = 50

     def announce_player(self):
        print(f"Powerful Mage {self.name} welcome ! You have {self.health}HP and {self.armor} armor!")


class Archer(Player):
     def __init__(self, name):
        super().__init__(name)
        self.health = 100
        self.armor = 80

     def announce_player(self):
        print(f"Sneeky Archer {self.name} welcome ! You have {self.health}HP and {self.armor} armor!")

        
print("Welcome to Echoes of the Abyss")
print("Let's create your character")
print("Select your class")

while True:
    user_choice = input("1.Warrior\n2.Mage\n3.Archer\n:> ")
    player1_name = input("Please give the name: ")

    if user_choice == "1":
        player1 =  Warrior(player1_name)
        player1.announce_player()
        break
    elif user_choice == "2":
        player1 = Mage(player1_name)
        player1.announce_player()
        break
    elif user_choice == "3":
        player1 = Archer(player1_name)
        player1.announce_player()
        break
    else:
        print("Please choose correct the class or you will be burn in hell!!!")



# player = Player(player1_name,player1_health)

# enemy = Player("Orc",100)

# Turns = 0
# while Turns <=5:
#     print("What you want to do next?: ")
#     print("\n1.Attack\n2.Show Healths\n3.End match ")
#     choice = str(input(":> "))

#     if choice == "1":
#         player.attack(enemy)
#         print("Attacking", end="", flush=True)
#         for i in range(3):
#             time.sleep(0.5)
#             print(".", end="", flush=True)
#         print()
#         player_damage = random.randint(0,100)
#         enemy.damage(player_damage)
#         if player_damage > 50:
#             player.counter_damage(random.randint(0,100))
#         Turns += 1
#         if player.is_dead() or enemy.is_dead():
#             if  player.is_dead() and enemy.is_dead():
#                 print("MASSACRE NO ONE SURVIVES!")
#                 break
#             else:
#                 if player.health > enemy.health:
#                     print(f"{player.name} WINS !!!")
#                     break
#                 elif enemy.health > player.health:
#                     print(f"{enemy.name} WINS !!!")
#                     break
#         else:
#             continue
        
                  
            
#     elif choice == "2":
#         player.show_health()
#         enemy.show_health()
    
#     elif choice == "3":
#         print(f"Match ended {player.name} has {player.health} remaining life and {enemy.name} has {enemy.health} remaining life")
#         if player.health > enemy.health:
#             print(f"{player.name} WINS !!!")
#         elif enemy.health > player.health:
#             print(f"{enemy.name} WINS !!!")
#         break

# if Turns == 5:
#     print("GAME OVER")
#     if player.health <=0 and enemy.health <= 0:
#         print("MASSACRE NO ONE SURVIVES!")
#     else:
#         if player.health > enemy.health:
#             print(f"{player.name} WINS !!!")
#         elif enemy.health > player.health:
#             print(f"{enemy.name} WINS !!!")


