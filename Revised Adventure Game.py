# Used his main  introduction to let IDE know to start from main
def main():
    player_name =(input("What's your name? "))
    print(" Welcome to this adventure game " + (player_name))
    
      
    
# Def is allowing me to define this function, for what I want to do
# I am using the defining function through the entire code, to allow each block of code to connect to one another smoothly
#  In the beginning, I could not get each block to intertwine. I ran into a multitude of problems ,but luckily found this method


def start_adventure():
    print(""" You are within the 1300s plague, you are one of two siblings that have been abandoned.You will have to approach
each situation carefully and help them survive the journey towards safety, while
standing clear of danger. Pick one of the siblings to be.""")
    sibling_pick = input("h for Hansel or g for Gretel ")
    if sibling_pick == 'h':
        print("You are Hansel\n")
        obstacleh_1()
    elif sibling_pick == 'g':
        print("You are Gretel\n")
        obstacleg_1()
    else:
        print("Please type h or g to select a sibling")
        start_adventure()
        
        
# I used the define function throughout this code to connect
# each section of code to one another, since I was having problems
# naking everything flow towards my ideal conclusion
        
def obstacleh_1():
        print("""You and Gretel are walking in the wilderness. Both
        of you see a wolf eating a carcass near a bush blocking your path""")
        print("""You want to throw a pebble to distract the wolf and Gretel want to
                sneak past it\n""")
        decide = input("What do you want to do? H for hansel, G for gretel ")
        if decide == "H":
            print(""" You throw a pebble, it surprisingly hits a tree, luring the wolf away
                    allowing you and Gretel to pass safely.\n""")
            obstacleh_2()
        if decide == "G":
            print(""" You and Gretel began to sneak pass the wolf. It snarls while eating its food
                    but does not look at you and surprisingly lets you both pass.\n""")
            
            
def obstacleg_1():
    print("""You and Hansel are walking in the wilderness. Both
        of you see a wolf eating a carcass near a bush""")
    print("Hansel wants to throw a pebble to distract it, you want to just sneak past")
    decide = input("What do you want to do? , H for hansel or G for gretel \n")
    if decide == "h":
        print("""Hansel throws a pebble, it surprisingly hits a tree bringing the wolf away
            allowing both of you to past safely.\n""")
        obstacleg_2()
    elif decide == "g":
        print(""" You and Hansel began to sneak passed the wolf. It snarls while both of you pass
            but, you still get the chance to sucessfully pass.\n""")
        obstacleg_2()
    else:
        print("please select h or g you route to be chosen")
        obstacleg_1()
        

def obstacleh_2():
    print(""" After passing the wolf, you and Gretel start to become hungry.
    You come across a bush of two berries. The left bush has plump purple fruit with green leaves on its stems.
    The right bush has orange-redish plump fruit that has sharp , prickly vines.
    What do you want to do?\n""")
    decide = input(" Type L for the left bush of berries, type R for the right bush, or N for neither. >")
    if decide == "L":
        print("""You and Gretel scoffed down the berries without a wait. Minutes later, you both felt rejuvenated and full of energy
        and ready to find shelter.\n""")
        obstacleh_3()
    elif decide == "R":
        print(""" You and Gretel scoffed down the berries without a wait. Seconds later, you felt groggy and sleepy, minutes later
        you felt sharp pain in your stomach. You check over to see Gretel unconscious. The pain your feeling intensifies raging on all over your
        upper-body. You unfortunatlely have a heart-attack, leaving Gretel alone.""")
        exit()
    elif decide == "N":
        print(""" You don't take the chance on the berries. You and your sister move-along to look
        look for shelter.\n""")
        obstacleh_3()
        
        

def obstacleg_2():
    print(""" After passing the wolf, You and Hansel start to become hungry. Luckily, you both
    come across a bush with two different berries. The left bush has plump purple fruit with green leaves on its stems.
    The right bush has a plump orange-redish plump fruit that has sharp prickly vines.
    What do you want to do?\n""")
    decide = input(" Type L for the left bush of berries. Type R for the right, or type N for neither. > ")
    if decide == "L":
         print("""You and Hansel scoffed down the berries without a wait. Minutes later, you both feel rejuvenated and full of energy
        and ready to find shelter\n""")
         obstacleg_3()
    elif decide == "R":
        print(""" You and Hansel scoffed down the berries without a wait. Seconds later, you feel groggy and sleepy, minutes later
        you feel a sharp pain in your stomach. You check next to you, to see Hansel unconscious. The pain your feeling intensifies raging on all over your
        upper-body. You unfortunatlely have a heart-attack, leaving Hansel alone""")
        print("Game Over")
        exit()
    elif decide == "N":
         print(""" You don't take the chance on the berries. You and your brother move-along to look
        look for shelter""")
         obstacleg_3()
         
         

def obstacleh_3():
    print("""You and Gretel walk for a while after the berry bushes. So much that your feet ache and you take small
    breaks from walking. The pain in you and your sister's feet abruptly dissapper after both of you come across a house.
    It is an odd looking house, but you think nothing of it. You and Gretel know on the door. There is no answer. Gretel wants
    to just go in since, she feels drops of rain upon her head, You want to look in the front window to see if anyone is inside.
    What do you do?""")
    decide = input(" Type S to enter the house or type W , to look in the window. > ")
    if decide == "S":
        print("""You and Gretel walk through the front door of the house. Both of you smell something incredibly appetizing, so much
        that it makes you both salivate. Both of you venture towards the smell and find a pie sitting on a table within a kitchen.
        Both of you all around the kitchen and house, while seeing no one.\n""")
    if decide == "W":
        print(""" You look through the front window and see no one. You tell Gretel and she still insist on entering, in which you agree upon
        reluctantly. Both of you smell something incredibly appetizing after entering, so much
        that it makes you both salivate. Both of you venture towards the smell and find a pie sitting on a table within a kitchen.
        Both of you look all around the kitchen and house, while seeing no one. \n""")
        obstacleh_4()
        
def obstacleg_3():
    print("""You and Hansel walk for a while after the berry bushes. So much that your feet ache and you take small
    breaks from walking. The pain in you and your brother's feet abruptly dissapper after both of you come across a house.
    It is an odd looking house, but you think nothing of it. You and Hansel knock on the door. There is no answer. Hansel wants
    to just go inside since, he feels drops of rain upon her head, You want to look in the front window to see if anyone is inside.
    What do you do?""")
    decide = input(" Type S to enter the house or type W , to look in the window. > ")
    if decide == "S":
        print("""You and Hansel walk through the front door of the house. Both of you smell something incredibly appetizing, so much
        that it makes you both salivate. Both of you venture towards the smell and find a pie sitting on a table within a kitchen.
        Both of you look all around the kitchen and house, while seeing no one.""")
        obstacleg_4()
    if decide == "W":
        print(""" You look through the front window and see no one. You tell Gretel and she still insist on entering, in which you agree upon
        reluctantly. Both of you smell something incredibly appetizing after entering, so much
        that it makes you both salivate. Both of you venture towards the smell and find a pie sitting on a table within a kitchen.
        Both of you look all around the kitchen and house, while seeing no one.""")
        obstacleg_4()
        

def obstacleh_4():
    print("""Gretel wants to eat the pie on the table. You want to as well, but the atmosphere doesn't seem right, so you tell her not to. She does
    not listen and sticks her finger into the pie, without you noticing. A figure glides down from the celing with a distorted face grabbing your sister.
    You pick up a chair from the kitchen and throw it at the figure, but it raises one of its' hands and pushes the chair away, then uses the same hand to
    throws you into a oven that has been turned on. /n""")
    print("You see three levers while in the oven. One has the insignia of a H, another has N, and the final has a R. What do you want to do? \n")
    decide = input("Type H for that insignia with that lever, type N for that lever, or R for that one. >")
    if decide == "H":
        print("""You pull the H lever and a gear activates retracting the other levers. You feel the oven began to become hotter. You start to burn and scream
        unfortunately, you were killed by the figure and Gretel was left to fight for herself.""")
        exit()
    if decide == "N":
        print(""" You pull the N lever and a gear activates retracting the lever you pulled. You feel the oven become hotter, but you have another option. Which
        lever would you like to pull next?""")
    if decide == "R":
        print(" You pull the R lever and a gear activates immediately releasing you from the oven. You exit the oven facing the back of the figure hold your sister")
        obstacleh_5()
        

def obstacleg_4():
    print("""Hansel wants to eat the pie on the table. You want to as well, but the atmosphere doesn't seem right, so you tell him not to. He does
    not listen and sticks his finger into the pie, without you noticing. A figure glides down from the celing with a distorted face grabbing your brother.
    You pick up a chair from the kitchen and throw it at the figure, but it raises one of its' hands and pushes the chair away, then uses the same hand to
    throws you into a oven that has been turned on. /n""")
    print("")
    print("You see three levers while in the oven. One has the insignia of a H, another has N, and the final has a R. What do you want to do? \n")
    decide = input("Type H for that insignia with that lever, type N for that lever, or R for that one. >")
    if decide == "H":
        print("""You pull the H lever and a gear activates retracting the other levers. You feel the oven began to become hotter. You start to burn and scream
        unfortunately, you were killed by the figure and Hansel was left to fight for himself.""")
        print("Game Over")
        exit()
    if decide == "N":
         print(""" You pull the N lever and a gear activates retracting the lever you pulled. You feel the oven become hotter, but you have another option. Which
        lever would you like to pull next?""")
         exit()
    if decide == "R":
        print("")
        print(" You pull the R lever and a gear activates immediately releasing you from the oven. You exit the oven facing the back of the figure hold your sister.\n")
        
        
        
def obstacleh_5():
    print("""You have the option of using a knife on the counter to stab the figure, then throw it into the agape oven
    (K), hitting the figure with your bare hands to save your sister(B), or using the knife, then calling for assistance from Gretel
    to push the figure into the oven (G) """)
    decide = input(" K for the first, B for the second, or G , for the third option")
    if decide == "K":
        print(""" You pick up a knife on the counter and stab the figure. It yells in pain, in which you consistently stab its back until it
        drops your sister. It does indeed drops Gretel giving you the chance to push it into the agape oven, while it was incapacitated.
        The figure yells and screeches in agonizing pain from it burning in the oven.""")
        print("")
        print("You and Gretel leave the house with the pie, surviving this fearful journey")
        print("You Win!!")
    if decide == "B":
        print("""You decide to punch the figure in the back, in which does nothing. The figure turns around, waving its hands again and throwing you
        back into the oven. No levers are found inside, which settles the end of your story. \n""")
        exit()
    if decide == "G":
        print(""" You pick up a knife on the counter and stab the figure. It yells in pain, in which you consistently stab its back until it
        drops Gretel. Gretel falls on the floor, in which you yell her name to help. She does and the figure is pushed into the oven. The
        figure screeches, while in agonizing pain from which no one hears. Since you and your sister have left with the pie, while being safe from danger.""")
        print("You Win!!")

      
        
def obstacleg_5():
    print("""You have the option of using a knife on the counter to stab the figure, then throw it into the agape oven
    (K), hitting the figure with your bare hands to save your brother(B), or using the knife, then calling for assistance from Hansel
    to push the figure into the oven (H) """)
    decide = input(" K for the first, B for the second, or G , for the third option")
    if decide == "K":
        print(""" You pick up a knife on the counter and stab the figure. It yells in pain, in which you consistently stab its back until it
        drops your brother. It does indeed drops Hansel, giving you the chance to push it into the agape oven, while it was incapacitated.
        The figure yells and screeches in agonizing pain from it burning in the oven.""")
        print("")
        print("You and Hansel leave the house with the pie, surviving this fearful journey")
    if decide == "B":
        print("""You decide to punch the figure in the back, in which does nothing. The figure turns around, waving its hands again and throws you
        back into the oven. No levers are found inside, which settles the end of your story \n""")
        print("Game Over")
        exit()
    if decide == "H":
        print(""" You pick up a knife on the counter and stab the figure. It yells in pain, in which you consistently stab its back until it
        drops Hansel. Hansel falls on the floor, in which you yell his name to help. She does and the figure is pushed into the oven. The
        figure screeches, while in agonizing pain from which no one hears. Since you and your brother have left with the pie, while being safe from danger.""")
        print("")
        print("You Win!!")
        
 
 






if __name__ == '__main__':
    main()
    
start_adventure()

    