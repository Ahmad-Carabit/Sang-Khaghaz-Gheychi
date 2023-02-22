#import
import random
#points
point = 0
system_point = 0

entekhab = ["sang","kaghaz","gheychi"]

while True:
    print("point : " +str(point))
    print("system_point : " +str(system_point))
    user_entekhab = input("beyn sang | kaghaz | gheychi | yeki ro entekhab kon  =>  ").lower()

    if user_entekhab not in entekhab:
        print("vorodi na dorost ast")
        continue

    random_system = random.randint(0,2)
    computer_entekhab = entekhab[random_system]
    print(f"entekhabe Computer ==> {computer_entekhab}")

    if user_entekhab == computer_entekhab:
        print(f"Mosavi Shodid !\n")

    elif user_entekhab == "sang" and computer_entekhab == "gheychi":
        print("barande shodi\n")
        point += 1

    elif user_entekhab == "kaghaz" and computer_entekhab == "sang":
        print("barande shodi\n")
        point += 1

    elif user_entekhab == "gheychi" and computer_entekhab == "kaghaz":
        print("barande shodi\n")
        point += 1

    else:
        print("shoma bakhtid\n")
        system_point += 1

#code by ahmad_carabit 
#Thank you for the star
