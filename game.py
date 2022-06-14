import random

# Strategies - setting variables/constants
NO_SWITCH = 'NO_SWITCH'
YES_SWITCH = 'YES_SWITCH'
RAND_SWITCH = 'RAND_SWITCH'

# define function measure_game, setting iteration to 10 as default if no iteration is selected. 
# Defining results lists per strategy
def measure_game(iterations=10):
  noSwitch = [] # dont switch door after a door is revealed
  yesSwitch = [] # switch door after a door is revealed
  randSwitch = [] # randomly decide to switch door after a door is revealed

  # Play game and record results
  for iter in range(iterations):
    noSwitch.append(play_game(NO_SWITCH))
    yesSwitch.append(play_game(YES_SWITCH))
    randSwitch.append(play_game(RAND_SWITCH))

  # report results
  print("No Switch: ", get_avg(noSwitch, iterations))
  print("Yes Switch: ", get_avg(yesSwitch, iterations))
  print("Rand Switch: ", get_avg(randSwitch, iterations))


# Game steps:
# place prize in one of 3 doors randomly
# pick one of 3 doors randomly
# reveal one of the other 2 doors
# reselct door based on strategy
# record win

def play_game(strategy):
  # place prize in one of 3 doors randomly
  prize = pick_random_door()
  # pick one of 3 doors randomly
  firstPick = pick_random_door()
  # reveal one of the other 2 doors
  revealedDoor = reveal_door(prize, firstPick)
  # reselect door based on strategy
  secondPick = make_second_choice(revealedDoor, firstPick, strategy)

  # record win
  hasWon = secondPick == prize
  return 1 if hasWon else 0


# Utils
def get_avg(results=[], iterations=10):
  total = 0
  for r in results:
    total += r

  return total / iterations

def pick_random_door():
  return random.randint(0,2)

def reveal_door(prize, firstPick):
  revealedDoor = 0
  for door in range(3):
    if prize != door and firstPick != door:
      revealedDoor = door
  return revealedDoor

def make_second_choice(revealedDoor, firstPick, strategy):
  secondChoiceDoors = get_second_choice_doors(revealedDoor)
  
  secondPick = firstPick
  if strategy == NO_SWITCH:
    secondPick = firstPick
  if strategy == YES_SWITCH:
    for door in secondChoiceDoors:
      if door != firstPick:
        secondPick = door
  if strategy == RAND_SWITCH:
    choiceIndex = random.randint(0, 1)
    secondPick = secondChoiceDoors[choiceIndex]
  
  return secondPick

def get_second_choice_doors(revealedDoor):
  secondChoiceDoors = []
  for door in range(3):
    if door != revealedDoor:
      secondChoiceDoors.append(door)
  return secondChoiceDoors


# run test
measure_game(100000)