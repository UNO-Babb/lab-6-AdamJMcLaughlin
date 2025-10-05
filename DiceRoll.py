#DiceRoll.py
#Name: Adam McLaughlin
#Date: Fall25
#Assignment: Lab06

import random  

def roll_dice_simulation():
    
    totals = [0] * 13  

    num_rolls = 10000

    
    for _ in range(num_rolls):
        
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        total = die1 + die2  
        totals[total] += 1  

    print("Results of rolling two dice 10,000 times:")
    print("Total   Count   Percentage")
    print("**************************")
    for total in range(2, 13):  
        count = totals[total]
        percentage = (count / num_rolls) * 100  
        print(f"{total:<7}{count:<8}{percentage:.2f}%")  

roll_dice_simulation()

