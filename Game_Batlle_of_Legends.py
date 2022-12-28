import random, os, time

# defining several variables
round_counter = 0
flag = True
player1credits = 100
player2credits = 100 

# warrior 1 sistem random generation
def warriors1():
  warriors = ["Achilles the Magnificent", "Ajax the Merciless", "Alexander the Great", "Evander the Beast", "Gunnar the Destroyer", "Maximus the Greatest", "Magnus the Almighty"]
  warrior1 = random.choice(warriors)
  return warrior1

# warrior 2 sistem random generation
def warriors2():
  warriors = ["Raven the Noble one", "Aretha the Excelente", "Andromeda the Ruler of men", "Artemis the Butcher", "Circe the Witch", "Electra the Sparkling one", "Valkyrie the Avenger"]
  warrior2 = random.choice(warriors)
  return warrior2

# defining player's warrior choice
def chosen_warrior(warrior):
  if warrior == 1:
    return (warrior1)
  else:
    return (warrior2)

# function to be used in the health and strength formulas
def roll_dice(side):
  result = random.randint(1, side)
  return result

# formula to generate warrior's healtth  
def health_stat():
  health = roll_dice(6) * roll_dice(12) / 2 + 10
  return health

# formula to generate warrior's strength
def strength_stat():
  strength = roll_dice(6) * roll_dice(8) / 2 + 12
  return strength

# calculating winning player's rounds bets by aproximation
def round_bets(player_bet_number):
  rounds_aproximation = abs(round_counter-player_bet_number)
  return rounds_aproximation

# resuming player's bets on battle
def battle_results():
  global player1credits, player2credits
  if player1_bet_winner == player2_bet_winner:
    print("Players tied on the battle bet\n")
  elif player1_bet_winner == "1":
    print(f"{player1name} won the battle bet ang got 10 credits from {player2name}.\n")
    player1credits += 10
    player2credits -= 10
  else:
    print(f"{player2name} won the battle bet ang got 10 credits from {player1name}.\n")
    player2credits += 10
    player1credits -= 10

# resuming player's bets on rounds
def rounds_results():
  global player1credits, player2credits
  if round_bets(player1_bet_rounds) == 0:
    print(f"{player1name} won the rounds bet by exact number andy got 20 credits from {player2name}.\n")
    player1credits += 20
    player2credits -= 20
  elif round_bets(player2_bet_rounds) == 0:
    print(f"{player2name} won the rounds bet by exact number and got 20 credits from {player1name}.\n")
    player1credits -= 20
    player2credits += 20
  elif round_bets(player1_bet_rounds) < round_bets(player2_bet_rounds):
    print(f"{player1name} won the rounds bet by approximation ang got 10 credits from {player2name}.\n")
    player1credits += 10
    player2credits -= 10
  else:
    print(f"{player2name} won the rounds bet by approximation ang got 10 credits from {player1name}.\n")
    player2credits += 10
    player1credits -= 10

# questioning the user to play again or end the game
def play_again():
  
  play_again = input("\nPlay again? (y/n): ")
  if play_again == "y":
    os.system("clear")
    return False
  else:
    print("\nGame Over!")
    exit()
    

print("⚔️  BATTLE OF LEGENDS ⚔️\n")
print("""*** About the Game ***
The system will randomly generate two warriors.
In each round the one who strikes the greatest number of hits will win.
The defeated warrior will lose wealth and strength.
Warriors will keep on fighting, many rounds, until one runs out of health or strength.
Players start the game with 100 credits each and should place bets
on the winning warrior and the number of battle rounds.
Players can bet on the same warrior, but not on the same number of rounds.

Bet's value:
Winning warrior: 10 credits

Number of rounds:
- By aproximantion: 10 credits
- Exact number: 20 credits""")

print("\n*** Player 1 ***")
player1name = input("Enter your name: ")
print (f"Hi {player1name},you have {player1credits} credits to play.")

print("\n*** Player 2 ***")
player2name = input("Enter your name: ")
print (f"Hi {player2name}, you have {player2credits} credits to play.\n")

while flag:  

  print("⚔️  These are the Legend warriors: ⚔️\n")
  
  warrior1 = warriors1()
  warrior1health = int(health_stat())
  warrior1strength = int(strength_stat())

  warrior2 = warriors2()
  warrior2health = int(health_stat())
  warrior2strength = int(strength_stat())

  warrior1Intelligence = round((warrior2health + warrior2strength) / 2)
  warrior2Intelligence = round((warrior1health + warrior1strength) / 2)

  health_damage = abs(warrior1strength-warrior2strength) + 1
  strength_damage = round(health_damage / 2)
  
  print("WARRIOR 1:", warrior1)
  print("- health:", warrior1health)
  print("- Strength:", warrior1strength)
  print("- Intelligence:", warrior1Intelligence)

  print("\nWARRIOR 2:", warrior2)
  print("- health:", warrior2health)
  print("- Strength:", warrior2strength)
  print("- Intelligence:", warrior2Intelligence)

  
  print("\nPlayers place your bets:\n")
    
  player1_bet_winner = int(input(f"{player1name}, bet the warrior (1/2): "))
  player1_bet_rounds = int(input("Bet the rounds: "))
  print(f"\n{player1name} you've bet on {chosen_warrior(player1_bet_winner)} to win the battle in {player1_bet_rounds} rounds")
   
  player2_bet_winner = int(input(f"\n{player2name}, bet the warrior (1/2): "))
  player2_bet_rounds = int(input("Bet the rounds: "))
  print(f"\n{player2name} you've bet on {chosen_warrior(player2_bet_winner)} to win the battle in {player2_bet_rounds} rounds")

  
  start = input("""\nAll set. May the battle begin...
press any key to start > """)
  if start != "":
    continue
  
  while True:
    round_counter += 1
    print(f"""
    
************************************
* 🗡️  FIGHT 🛡️  FIGHT 🔪 FIGHT 🏹    *
*            Round: {round_counter}              *
************************************
""")
    
    warrior1strikes = roll_dice(6)
    warrior2strikes = roll_dice(6)
    print(warrior1, "\n- Number of strikes:", warrior1strikes)
    print("")
    print(warrior2, "\n- Number of strikes:", warrior2strikes)
    print("")
    
    if warrior1strikes > warrior2strikes:
      print(warrior1,"wins round", round_counter)
      warrior2health -= health_damage + round(warrior1Intelligence / 9)
      warrior2strength -= strength_damage + round(warrior1Intelligence / 9)
      print(f"\n{warrior2}, takes damage, and now has {warrior2health} health and {warrior2strength} strength")
            
      if warrior2health <= 0 or warrior2strength <= 0:
        print("""
        *********************************
        *       WARRIOR 2 IS DEAD       *
        *********************************
        """)
        print(f"Warrior 1: {warrior1}, won the battle in {round_counter} rounds\n")
        # resuming player's bets on battle
        battle_results()
        # resuming player's bets on rounds
        rounds_results()
        # resuming player's credits
        print(f"{player1name} total credits: {player1credits}\n{player2name} total credits: {player2credits}\n")
        # questining the user to play again or end the game
        play_again = input("\nPlay again? (y/n): ")
        if play_again == "y":
          os.system("clear")
          print (f"{player1name}, your credit balance is {player1credits} credits")
          print (f"{player2name}, your credit balance is {player2credits} credits\n")
          break
        else:
          print("\nGame Over!")
          exit()
            
    elif warrior1strikes < warrior2strikes:
      print(warrior2,"wins round", round_counter)
      warrior1health -= health_damage + round(warrior2Intelligence / 10)
      warrior1strength -= strength_damage + round(warrior2Intelligence / 10)
      print(f"{warrior1} takes damage, and now has {warrior1health} health and {warrior1strength} strength")
             
      if warrior1health <= 0 or warrior1strength <= 0:
        print("""
        *********************************
        *       WARRIOR 1 IS DEAD       *
        *********************************
        """)
        print(f"Warrior 2: {warrior2}, won the battle in {round_counter} rounds\n")
        # resuming player's bets on battle
        battle_results()
        # resuming player's bets on rounds
        rounds_results()
        # resuming player's credits
        print(f"{player1name} total credits: {player1credits}\n{player2name} total credits: {player2credits}\n")
        # questioning the user to play again or end the game
        play_again = input("\nPlay again? (y/n): ")
        if play_again == "y":
          os.system("clear")
          print (f"{player1name}, your credit balance is {player1credits} credits")
          print (f"{player2name}, your credit balance is {player2credits} credits\n")
          break
        else:
          print("\nGame Over!")
          exit()
                 
    else:
      print("That was a Draw")
