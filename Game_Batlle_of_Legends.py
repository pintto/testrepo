import random, os, time


def warriors1():
    warriors = ["Achilles the Magnificent", "Ajax the Merciless", "Alexander the Great", "Evander the Beast",
                "Gunnar the Destroyer", "Maximus the Greatest", "Magnus the Almighty"]
    warrior1 = random.choice(warriors)
    return warrior1


def warriors2():
    warriors = ["Raven the Noble one", "Aretha the Excelente", "Andromeda the Ruler of men", "Artemis the Butcher",
                "Circe the Witch", "Electra the Sparkling one", "Valkyrie the chooser of Slain"]
    warrior2 = random.choice(warriors)
    return warrior2


def roll_dice(side):
    result = random.randint(1, side)
    return result


def health_stat():
    health = roll_dice(6) * roll_dice(12) / 2 + 10
    return health


def strength_stat():
    strength = roll_dice(6) * roll_dice(8) / 2 + 12
    return strength


round_counter = 0
flag = True
while flag:
    # round_counter += 1
    print("⚔️  BATTLE OF LEGENDS ⚔️\n")
    print("""Warriors will fight until one runs out of health, and that means Death!
  """)

    warrior1 = warriors1()
    warrior1health = int(health_stat())
    warrior1strength = int(strength_stat())

    warrior2 = warriors2()
    warrior2health = int(health_stat())
    warrior2strength = int(strength_stat())

    health_damage = abs(warrior1strength - warrior2strength) + 1

    print("WARRIOR 1:", warrior1)
    print("health:", warrior1health)
    print("Strength:", warrior1strength)

    print("\nWARRIOR 2:", warrior2)
    print("health:", warrior2health)
    print("Strength:", warrior2strength)

    start = input("""
May the battle begin...
press any key to start > """)
    if start != "":
        continue

    while True:
        print("\n🗡️  FIGHT 🛡️  FIGHT 🔪 FIGHT 🏹\n")
        round_counter += 1
        warrior1strikes = roll_dice(6)
        warrior2strikes = roll_dice(6)
        print(warrior1, "\n- Number of strikes:", warrior1strikes)
        print("")
        print(warrior2, "\n- Number of strikes:", warrior2strikes)
        print("")

        if warrior1strikes > warrior2strikes:
            print(warrior1, "wins round", round_counter)
            print("Warrior 1 health =", warrior1health, "\n")
            print(warrior2, "takes a hit with", health_damage, "damage")
            warrior2health -= health_damage
            print("Warrior 2 health =", warrior2health)

        elif warrior1strikes < warrior2strikes:
            print(warrior2, "wins round", round_counter)
            print("Warrior 2 health =", warrior2health, "\n")
            print(warrior1, "takes a hit, with", health_damage, "damage")
            warrior1health -= health_damage
            print("Warrior 1 health =", warrior1health)

        else:
            print("That was a Draw")

        new_round = input("\nGo to next round? (y/n): ")
        if new_round == "n":
            exit_game = input("Exit the game? (y/n): ")
            if exit_game == "y":
                print("Game over!")
                flag = False
                break
        else:
            print("\nThe battle continues!")
            continue
