from time import sleep
from assets.shelp import shelp
from sys import stdout

currentchars = {}
openedchests = {} # room:chests
currentroom = 0
inventory = []
equipped = {"gun":""}
gold = 0
status = {"inbattle":False,"health":10}
roomdesc = ""
enemyhealth = 0
dmgpershot = 0
enemyspoils = [""]
nextroom = 0
lastroom = 0

guns = {"LG16":2,"gun":1,"SR4":3}

def msgbox(string): # copy-pasted from loom encryption
    print("┌"+"─"*(len(string)+4)+"┐")
    print("│  "+string+"  │")
    print("└"+"─"*(len(string)+4)+"┘")

def typewrite(string):
    for i in string:
        print(i,end="")
        stdout.flush()
        sleep(0.01)
    print("")

def menu():
    ans = ""

    print("Welcome to...")
    print("""

   _____ ____  ___    ___    ___   ____________
  / ___// __ \/   |  /   |  /   | / ____/ ____/
  \__ \/ /_/ / /| | / /| | / /| |/ /   / __/   
 ___/ / ____/ ___ |/ ___ |/ ___ / /___/ /___   
/____/_/   /_/  |_/_/  |_/_/  |_\____/_____/   

           an ascii adventure game
                 v1.0 (beta)
                                               
    """)
    print("\n")
    print("What would you like to do?\n\n")
    print("1. play spaaace")
    print("2. how to play")
    print("3. quit because you know you don't want to be here")
    while True: # replace with better method later on
        ans = input("> ")
        if ans == "1":
            game() #filesystem somehow
        elif ans == "2":
            shelp()
        elif ans == "3":
            exit()



def draw(roomnum):
    global currentchars
    global currentroom
    global roomdesc
    global enemyhealth
    global dmgpershot
    global enemyspoils
    global status
    global nextroom
    global enemyname

    currentroom = roomnum

    if roomnum == 1:
        print("""
###############
#  C          #
#      @      D
#    [__]     #
###############       
        """)
        currentchars = {"c":"gun","d":2}
        roomdesc = "You are in a futuristic hospital room with a door on your right and a chest to your northwest."
    elif roomnum == 2:
        currentchars = {"c":"LG16","d":1,"d2":256,"i":"Welcome to space. In the chest, there is a laser gun. Please take it! You will need it to survive."}
        roomdesc = "You are in a long hall with an information hologram in front of you. There is a chest right next to it and a door leading out."
        print("""
#########################
#                       #
D @    I                D2
#      C                #
#########################
        """)
    elif roomnum == 3:
        currentchars = {"d":4,"x":""}
        roomdesc = "You have just killed a target. Nice one."
        print("""
#####################
#                   #
# @     X           D
#                   #
#####################
        """)
    elif roomnum == 4:
        currentchars = {"d":3,"d2":5,"d3":6,"i":"Ah, your first choice. Choose wisely."}
        roomdesc = "There are two doors ahead."
        print("""
#####################
#         I         D2
D @                 #
#                   D3
#####################
        """)
    elif roomnum == 5:
        currentchars = {"c":"_item_0xa8f099","i":"      "}
        roomdesc = "                            "
        print("""
##########
#    I   #
# @      #
#      C #
##########
        """)
    elif roomnum == 6:
            currentchars = {"d":257,"d2":0,"d3":0,"s":0,"i":"Great choice! Now, your real adventure begins."}
            roomdesc = "Doors everywhere."
            print("""
#####S####D##########
#                   #
#    I     @        D2
#                   #
##########D##########
          3
            """)
    elif roomnum == 7:
            currentchars = {"d":0,"d2":0,"d3":0,"i":""}
            roomdesc = ""
            print("""
##########D##########
#                   #
#    I     @        D2
#                   #
##########D##########
          3
            """)
    elif roomnum == 8:
        currentchars = {"d":0,"i":"Please keep in mind that this game isn't done lol - Nanobot567"}
        roomdesc = ""
        print("""
#####################
#         I         #
#         @         #
#    X              #
##########D##########
          
        """)
    elif roomnum == 255:
        currentroom = 255
        print("""
###############
#             #
#   testroom  #
#             #
###############
        """)
        currentchars = {"c":"","d":0}

    # enemy shooting rooms

    elif roomnum == 256:
        currentroom == 256
        status["inbattle"] = True
        enemyhealth = 1
        dmgpershot = 0
        enemyspoils = ["10G"]
        nextroom = 3
        print("""
 #####
#     #
#  #  #
#     #
 #####   
        """)
    elif roomnum == 257:
        currentroom == 257
        status["inbattle"] = True
        enemyhealth = 5
        dmgpershot = 0.5
        enemyspoils = ["air"]
        nextroom = 8
        print("""
   @
  /|\\
 / | \\
        """)

    msgbox(roomdesc)

def shop(num):
    global roomdesc
    global currentroom
    global currentchars
    global inventory
    global openedchests
    global guns
    global equipped
    global gold


    print("Welcome to my shop! What would you like to buy?\n")
    if num == 0:
        while int(ans) != 3:
            while not int(ans).isnumeric:
                print("1. SR4 (type gun, 3 dmg) [Price: 20G]")
                print("2. 10G [Price: 1G]")
                print("3. Leave")
                ans = input()
            if int(ans) == 1 and (gold == 20 or gold > 20):
                equipped["gun"] = "SR4"
                gold -= 20
                print("Thanks for your purchase! Can I get you anything else?")
            elif int(ans) == 1:
                gold -= 1
                print("Lol get scammed")
    print("Come back soon!")
            

            


def openchest():
    global roomdesc
    global currentroom
    global currentchars
    global inventory
    global openedchests
    global guns
    global equipped
    global gold

    try:
        if currentchars["c"] in openedchests[currentroom]:
            print("The chest is empty.")
    except KeyError:    
        chestitem = currentchars["c"]   
        if chestitem in guns:
            equipped["gun"] = chestitem
            print(f"Equipped {currentchars['c']}")
        else:
            inventory.append(chestitem)
            print(f"Added {chestitem}")

        openedchests[currentroom] = currentchars["c"]
    
    if "_item_0xa8f099" == currentchars["c"]:
        inventory.clear()
        equipped.clear()
        openedchests.clear()
        print("\n"*1000)
        menu()


def game():
    global currentchars
    global currentroom
    global roomdesc
    global enemyhealth
    global dmgpershot
    global enemyspoils
    global status
    global openedchests
    global lastroom
    global guns
    global equipped
    global gold


    cmd = ""

    print("\n"*1000)
    sleep(4)
    print("- 24XX -\n")
    sleep(1)
    typewrite("A warrior from a long-gone planet called Earth wakes up from a long slumber.\nThey don't remember much about themself, but thankfully there is a mirror nearby to help them re-discover their identity.") #typewriter effect :O
    sleep(1)
    typewrite("\nWho am I?")
    name = input("> ")
    # print("\nWhat is my shirt color?")
    # shirt = input("> ") # basic customization

    typewrite(f"Ah, yes, {name}. That is your name. And your name is {name}. Awesome.")
    typewrite("A door stands ajar on your right. It is now that your journey begins.\n\n")
    
    draw(1)

    while True:
        
        cmd = input("> ")
        if cmd in currentchars:
            if cmd == "d":
                lastroom = currentroom
                draw(currentchars["d"])
            elif cmd == "d2":
                lastroom = currentroom
                draw(currentchars["d2"])
            elif cmd == "d3":
                lastroom = currentroom
                draw(currentchars["d3"])
            elif cmd == "c":
                openchest()
            elif cmd == "i":
                print(currentchars["i"])
            elif cmd == "x":
                print("A corpse.")
            elif cmd == "s":
                shop(currentchars["s"])
        elif cmd == "redraw":
            draw(currentroom)
            

        elif cmd == "quit":
            exit()

        elif cmd == "inv" or cmd == "inventory":
            typewrite("You are currently holding:")
            for i in inventory:
                typewrite(i)
            typewrite("Currently equipped:")
            for i in equipped:
                typewrite(f"Gun: {equipped['gun']} (atk: {guns[equipped['gun']]})")
            typewrite(f"Gold: {gold}")
    
        elif cmd == "help":
            shelp()


        

        if status["inbattle"]:
            ctr = 0
            if equipped["gun"] in guns:
                print("PRESS ENTER TO SHOOT!")
            else:
                print("PRESS ENTER TO PUNCH!")

            while enemyhealth != 0:
                if status["health"] == 0 or status["health"] < 0:
                    typewrite("YOU DIED!")
                    status["inbattle"] = False
                    draw(lastroom)
                    break
                    
                if enemyhealth == 0 or enemyhealth < 0:
                    break


                input("> ")
                if equipped["gun"] in guns:
                    enemyhealth -= guns[equipped["gun"]]
                else:
                    enemyhealth -= 1
                ctr += 1
                status["health"] = status["health"] - dmgpershot

                print(f"HEALTH: {status['health']}")
                print(f"ENEMY HEALTH: {enemyhealth}")
            
            if status["inbattle"] == True:
                print("YOU WON! You got:")
                for i in enemyspoils:
                    print(i)
                    if i.endswith("G"):
                        gold += int(i.split("G")[0])
                    else:
                        inventory.append(i)
                status["inbattle"] = False
                draw(nextroom)

            
                

    

menu()