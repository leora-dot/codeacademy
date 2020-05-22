# Code Academy puts these values before the code. 
import random
money = 100
#Write your game of chance functions here:

# These mini-functions help the chance functions run. The bet_validation and double_validations confirm that the bet and guess values entered by the player are valid. The win and lose functions adjust money and print text for each scenario. The card_value function assigns numerical value to a card chosen from a standard deck. 

def bet_validation(bet):
  if bet<0:
    print ("No shorting allowed! Bet a positive value.")
    return
  elif bet>money:
    print ("No loans here! You can't bet more than you've got.")
    return
  else:
    return True

def double_validation(correct_val1,correct_val2,text):
  if text == correct_val1 or text == correct_val2:
    return True
  else:
    print("You need to guess "+correct_val1+" or "+correct_val2+". You guessed "+text+".")
    return

def win(bet, odds = 1):
  global money
  money += bet*odds
  print("You won, hotshot! You won $" + str(bet*odds) + ", and now you have $" + str(money)+".")

def lose(bet, odds = 1):
  global money
  money -= bet*odds
  if money >=0:
    print("You lost, sad-pants! You lost $" + str(bet*odds) + ", and now you have $" + str(money)+".")
  else:
    money = 0
    print ("You lost, sad-pants! You lost $" + str(bet*odds) + ", and now you have no money to pay off your gambling debt.")

def card_value(card):
  if(card[0]) == "a":
    card_value = 1
  elif(card[0:2]) == "ja":
    card_value = 11
  elif(card[0]) == "q":
    card_value = 12
  elif(card[0]) == "k":
    card_value = 13
  elif(card[0:2]) == "jo":
    card_value = 1
  else:
    card_value = card[0:2]
  card_value = int(card_value)
  return card_value

# There are the actual chance games: 

#Create a function that simulates flipping a coin and calling either "Heads" or "Tails". This function (along with all of the other functions you will write in this project) should have a parameter that represents how much the player is betting on the coin flip.

def coin(guess,bet):
  # This section validates values for guess and bet
  if bet_validation(bet) == True:
    pass
  else:
    return
  if double_validation("heads","tails",guess) == True:
    guess = guess
  else:
   return
  # This section flips the coin. Heads is one and tails is zero.  
  coin = random.randint(0,1)
  if coin == 1:
    coin = "heads"
  else:
    coin = "tails"
  # This section compares the player's guess to the flipped coin value and announces the result. 
  print("You bet $" + str(bet) +" that the coin flip would come up " + guess+", and the coin was "+coin+".")
  if guess == coin:
    win(bet)
  else:
    lose(bet)

# Create a function that simulates playing the game Cho-Han. The function should simulate rolling two dice and adding the results together. The player predicts whether the sum of those dice is odd or even and wins if their prediction is correct.

def chohan(guess,bet):
   # This section validates values for guess and bet
  if bet_validation(bet) == True:
    pass
  else:
    return
  if double_validation("even","odd",guess) == True:
    pass
  else:
   return
 # This section rolls both dice and evaluates whether the sum is odd or even
  die1 = random.randint(1,6)
  die2 = random.randint(1,6)
  dice_sum = die1+die2
  if dice_sum%2 == 0:
    result = "even"
  else:
    result = "odd"
  # This section compares the player's guess to the dice and announces the results
  print("You bet that the Cho-Han dice would be "+guess+". You rolled a "+str(die1)+" and a "+str(die2)+", which add up to "+str(dice_sum)+", which is "+result+".")
  if result == guess:
    win(bet)
  else:
    lose(bet)

# Create a function that simulates two players picking a card randomly from a deck of cards. The higher number wins

def card_pick(bet):
   # This section validates the bet
  if bet_validation(bet) == True:
    pass
  else:
    return
  # This section generates the list of cards in a standard deck, 52 cards plus two jokers. 
  card_suites = ["hearts", "spades", "diamonds", "clubs"]
  card_numbers = ["ace","jack","queen","king"] + list(range(2,11))
  available_cards = []
  for number in card_numbers:
    for suite in card_suites:
      available_cards.append(str(number)+" of "+suite)
  for i in range(2):
    available_cards.append("joker")
  # This section selects cards for both the player and the opponent. 
  player_card = available_cards[random.randint(0, len(available_cards)-1)]
  player_card_value = card_value(player_card)
  available_cards.remove(player_card)
  opponent_card = available_cards[random.randint(0, len(available_cards)-1)]
  opponent_card_value = card_value(opponent_card)
  ## This section compares the two cards and announces results. 
  print("You bet you'd pick the better card. You picked the "+player_card+" ("+str(player_card_value)+" points), and your opponent picked the "+opponent_card+" ("+str(opponent_card_value)+" points).")
  if player_card_value > opponent_card_value:
    win(bet)
  elif player_card_value < opponent_card_value:
    lose(bet)
  else:
    print ("It's a tie! Play again?")

# Create a function that simulates some of the rules of roulette. A random number should be generated that determines which space the ball lands on.

def roulette(guess, bet):
   # This section validates the bet
  if bet_validation(bet) == True:
    pass
  else:
    return
  # This section lists the numbers on the wheel and the states odd and even. 
  numbers_available = [2, 14, 35, 23, 4, 16, 33, 21, 6, 18, 31, 19, 8, 12, 29, 25, 10, 27, 13, 36, 24, 3, 15, 34, 22, 5, 17, 32, 20, 7, 11, 30, 26, 9, 28,1,0, "00"]
  evenness = ["odd","even"]
  # This section spins the wheel
  number_landed = numbers_available[random.randint(0,len(numbers_available))]
  # This section validates the player's guess
  acceptable_guesses = numbers_available + evenness
  try:
    acceptable_guesses.index(guess)
  except:
    print ("You need to guess odd, even, or one of the numbers on a roulette wheel. You guessed "+str(guess)+".")
    # This section evaluates whether the player bet on odds/evens and completes the game, if so. Spinning the 0 and 00 values causes the player to lose. 
  if guess == "odd" or guess == "even":
      print("You guessed the ball would land on an "+str(guess)+" number, and it landed on "+str(number_landed)+".")
      if number_landed == 0 or number_landed == "00":
        lose(bet)
      elif (number_landed%2 == 0 and guess == "even") or (number_landed%2 == 1 and guess == "odd"):
        win(bet)
      else:
        lose(bet)
  # This section completes the game if a player has bet on a specific number. Odds for these bets are 1:35. 
  else:
    odds = 35
    print("You guessed the ball would land on "+str(guess)+", and it landed on "+str(number_landed)+".")
    if number_landed == guess:
      win(bet,odds)
    else:
      lose(bet,odds)
  
#Call your game of chance functions here
coin("heads",12)
chohan("even",24)
card_pick(10)
roulette(14,1)
