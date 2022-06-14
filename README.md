**Description:**
While on a road trip, the discussion of the Monty Hall problem came up and it seemed impossible that switching doors after one was revealed was more advantageous than sticking with your original door.
So we wrote this script in the car without much internet to prove our hypothesis: that it is not more advantageous to switch doors.
This simulates the game played using 3 different strategies:
1. No Switch - Don't switch door after a door is revealed.
2. Switch - Always switch doors after a door is revealed.
3. Random Switch - Randomly decide to switch doors after one is revealed. 50% of the time switch, 50% of the time don't switch.

The game is repeated n number of times and the outcomes (who won) for each of the 3 different strategies are recorded.

The average wins are then reported for each strategy.

**How to play:**
`python3 game.py`

- To change the number of iterations, edit the integer passed into the measure_game call at the end of game.py.

**Results:**
As more games are played, the averages settle on:
- No Switch: win 33% of the time
- Always Switch: win 66% of the time
- Randomly Switch: win 50% of the time

**Conclusion:**
We were wrong! It _is_ better to always switch.

While writing this script, it became clear why never switching is not advantageous. When the game host reveals an empty door, he will never open the door that the contestant picks, regardless if it has the prize or not. Therefore, the propability that the prize is in the door that was first picked does not change after the empty door is revealed. Only the other remaining door has a higher chance that it contains the prize.

At least that helped us wrap our heads around it!