from Zombie_Game.character import Character
dave=Enemy("Dave", "A stinkin zombie")

dave.desrcibe()

dave.set_conversation("Hello there! I am going to join your OOP game very soon")

dave.talk()

from Zombie_Game.character import Enemy

dave.set_weakness("sun")

print("What will you fight with?")
fight_with = input()
dave.fight(fight_with)

