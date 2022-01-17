#Kiran Adhikari
#COMP 1405-C
#Assignment 2: Lootbox 
# Note: I have changed my crate rarity and it is slightly different from the Professor's example:
# Note: Instead of Common, Rare, Epic - My order of crates are: 1.(Common) 2.(Uncommon) 3.(Rare)
# Note: The currencey used is Soul(s), instead of regular $(s). I did this to incorporate more details from the Bleach anime (crate names too)

import random
crate_one = "[Common] Hollow Crate"
crate_two = "[Uncommon] Bankai Crate"
crate_three = "[Rare] Final Getsuga Tenshou Crate"
price_one = "[2.50 Souls each]"
price_two = "[4.50 Souls each]"
price_three = "[8.50 Souls each]"
FINALONE = 0
FINALTWO = 0
FINALONEPRICE = 0
FINALTWOPRICE = 0
FINALTHREEPRICE = 0
FINALTHREE = 0
CRATE_NUM1 =0
CRATE_NUM2 = 0
CRATE_NUM3 = 0
notquit = False
# x = n.o crates & y = crate type
def open_box(x,y):
    for i in range (3):
        randomnum1 = random.random()
        if y == 'Hollow Crate':
            if int(x) > 0:
                if randomnum1 <= 0.8:
                    print("You got a Common Item!")
                elif randomnum1 < 0.95:
                    print ("You got an Uncommon Item!")
                else:
                    print("You got a Rare item!")
    
        elif y == 'Bankai Crate':
            if int(x) > 0:
                if randomnum1 <= 0.5:
                    print("You got a Common Item!")
                elif randomnum1 < 0.9:
                    print ("You got an Uncommon Item!")
                else:
                    print("You got a Rare item!")
    
        elif y == 'Final Getsuga Tenshou Crate':
            if int(x) > 0:
                if randomnum1 <= 0.3:
                    print("You got a Common Item!")
                elif randomnum1 < 0.80:
                    print ("You got an Uncommon Item!")
                else:
                    print("You got a Rare item!")
    i += 1
        
player_name = input("Welcome to the 'Bleach' World AKA 'Soul Society'. Please enter your player name:")
print("Greetings,", player_name)

while not notquit:
    crate_select= input("Please select the following crates you would like to purchase (1-3):\n1. [Common] Hollow Crate [2.50 souls] \n2. [Uncommon] Bankai Crate [4.50 souls] \n3. [Rare] Final Getsuga Tenshou Crate [8.50 souls]\n4. Complete Purchase\n")   
    if crate_select == '1':
        CRATE_NUM1= "a"
        while not CRATE_NUM1.isdigit():
            CRATE_NUM1= (input("How many {0} Crates {1} would you like to purchase?\n".format(crate_one, price_one)))
            if not CRATE_NUM1.isdigit():
                CRATE_NUM1= (input("Please enter a positive number! How many {0} Crates {1} would you like to purchase?\n".format(crate_one, price_one)))
                continue
        FINALONE += int(CRATE_NUM1)
        FINALONEPRICE = (FINALONE * 2.50)
    
    elif crate_select == '2':
        CRATE_NUM2= "b"
        while not CRATE_NUM2.isdigit():
            CRATE_NUM2= (input("How many {0} Crates {1} would you like to purchase?\n".format(crate_two, price_two)))
            if not CRATE_NUM2.isdigit():
                CRATE_NUM2= (input("Please enter a positive number! How many {0} Crates {1} would you like to purchase?\n".format(crate_two, price_two)))
                continue
        FINALTWO += int(CRATE_NUM2)
        FINALTWOPRICE = (FINALTWO * 4.50)

    elif crate_select == '3':
        CRATE_NUM3= "c"
        while not CRATE_NUM3.isdigit():
            CRATE_NUM3= (input("How many {0} Crates {1} would you like to purchase?\n".format(crate_three, price_three)))
            if not CRATE_NUM3.isdigit():
                CRATE_NUM3= (input("Please enter a positive number! How many {0} Crates {1} would you like to purchase?\n".format(crate_three, price_three)))
                continue
        FINALTHREE += int(CRATE_NUM3)
        FINALTHREEPRICE = (FINALTHREE * 8.50)
    
    elif crate_select == '4':
        total_price = float((FINALONE * (2.50)) + (FINALTWO * (4.50)) + (FINALTHREE * (8.50)))
        if int(CRATE_NUM1) > 0 and int(CRATE_NUM2) > 0 and int(CRATE_NUM3) > 0:
        
            print("Thank you!, here is your receipt:\n-------------------------------------\n{0}x   {1}     {2} Souls".format(FINALONE, crate_one, FINALONEPRICE))
            print("{0}x   {1}     {2} Souls".format(FINALTWO, crate_two, FINALTWOPRICE))
            print("{0}x   {1} Souls     {3} Souls\n\nTotal Cost: {2} Souls\n-------------------------------------".format(FINALTHREE, crate_three, total_price, FINALTHREEPRICE))
        
        elif int(CRATE_NUM1) > 0 and int(CRATE_NUM2) > 0:
            print("Thank you!, here is your receipt:\n-------------------------------------\n{0}x   {1}     {2} Souls".format(FINALONE, crate_one, FINALONEPRICE))
            print("{0}x   {1}     {2} Souls".format(FINALTWO, crate_two, FINALTWOPRICE))
            print ("\nTotal Cost: {} Souls".format(total_price))
        
        elif int(CRATE_NUM2) > 0 and int(CRATE_NUM3) > 0:
            print("Thank you!, here is your receipt:\n-------------------------------------\n{0}x   {1}     {2} Souls".format(FINALTWO, crate_two, FINALTWOPRICE))
            print("{0}x   {1} Souls     {3} Souls\n\nTotal Cost: {2} Souls\n-------------------------------------".format(FINALTHREE, crate_three, total_price, FINALTHREEPRICE))
        
        elif int(CRATE_NUM1) > 0 and int(CRATE_NUM3) > 0:
            print("Thank you!, here is your receipt:\n-------------------------------------\n{0}x   {1}     {2} Souls".format(FINALONE, crate_one, FINALONEPRICE))
            print("{0}x   {1} Souls     {3} Souls\n\nTotal Cost: {2} Souls\n-------------------------------------".format(FINALTHREE, crate_three, total_price, FINALTHREEPRICE))
        
        elif int(CRATE_NUM1) > 0:
            print("Thank you!, here is your receipt:\n-------------------------------------\n{0}x   {1}     {2} Souls".format(FINALONE, crate_one, FINALONEPRICE))
            print ("\nTotal Cost: {} Souls\n-------------------------------------".format(total_price))
        
        elif int(CRATE_NUM2) > 0:
            print("Thank you!, here is your receipt:\n-------------------------------------\n{0}x   {1}     {2} Souls".format(FINALTWO, crate_two, FINALTWOPRICE))
            print ("\nTotal Cost: {} Souls\n-------------------------------------".format(total_price))
        
        elif int(CRATE_NUM3) > 0:
            print("Thank you!, here is your receipt:\n-------------------------------------\n{0}x   {1}     {2} Souls".format(FINALTHREE, crate_three, FINALTHREEPRICE))
            print ("\nTotal Cost: {} Souls\n-------------------------------------".format(total_price))
        
        else:
            print("You did not purchase anything. Come back again :)")
        
        notquit = True

if int(FINALONE) > 0 or int(FINALTWO) > 0 or int(FINALTHREE) > 0:
    print("Now we open the crates!\n")
cratesin1 = 0
for cratesin1 in range (int(FINALONE)):
    print("Opening [Common] Hollow Crate #", cratesin1 + 1)
    open_box(int(FINALONE), 'Hollow Crate')

cratesin2 = 0
for cratesin2 in range (int(FINALTWO)):
    print("Opening [Uncommon] Bankai Crate #", cratesin2 + 1)
    open_box(int(FINALTWO), 'Bankai Crate')
    
cratesin3 = 0
for cratesin3 in range (int(FINALTHREE)):
    print("Opening [Rare] Final Getsuga Tenshou Crate #", cratesin3 + 1)
    open_box(int(FINALTHREE), 'Final Getsuga Tenshou Crate')

input("Press enter to quit")