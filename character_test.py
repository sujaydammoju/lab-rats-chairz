from character import *

dave = Enemy("Dave", "A smelly zombie")
dave.set_weakness("cheese")

dave.describe()
print("What will you fight with?")
fight_with = input()
dave.fight(fight_with)

