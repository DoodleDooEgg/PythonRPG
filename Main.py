import time
print("game start")
time.sleep(.5)
name = input("Choose your name: ")
print("\n\nIt is 1789")
print("\nYou are "+name)
time.sleep(1)
print("\nYou are a professional assasin in America")
time.sleep(3)
print("\nYou have deep hatred for the Americans after they colonised the New World")
time.sleep(3)
print("\nYou are ordered to assasinate a high profile figure.")
time.sleep(3)
print("\nYour boss tells you..")
time.sleep(2)
print("\n"+"'"+name+", I want you to assasinate the man who will become president, to give me a chance to become president myself!'")
time.sleep(2)
print("\nYou leave the house and make your way down to the adress that was written on a note your boss gave you..")
time.sleep(2)
print("\n.. '1600 Pennsylvania Avenue NW in Washington, D.C'")
time.sleep(1)
print("\nUpon arriving, you break into the mansion and in there you find the military general.")


# enemy encounter 1 
time.sleep(1)
print("\nThis is General Chungus")
battle = input("\nBattle General Chungus? Type either Yes or No: ")

fight = "Yes"
run = "No"

if battle == run:
    print("You have failed your mission.")

elif battle == fight:
    print("You have engaged in a fight with Enemy 1.")
    time.sleep(1)
    print("You have three attacks: Slash, Piercing Stab, and Pistol Shot.")
    time.sleep(1)
    attack = input("Choose an attack from Slash, Piercing Stab, or Pistol Shot: ")

    if attack == "Slash":
        print("You slash at the General with your hidden blade but you miss, losing the fight.")
    elif attack == "Piercing Stab":
        print("You lunge forward and stab the General with precision!")
    elif attack == "Pistol Shot":
        print("You draw your pistol and fire a deadly shot!")
    else:
        print("You hesitate and miss your opportunity to attack!")
