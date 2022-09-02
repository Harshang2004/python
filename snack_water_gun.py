import random
print("----snack water gun game----")
list = ["SNACK","WATER","GUN"]
you = 0
com = 0
tie = 0
chance = 10
n = 1

def computerr():
    print(f"{n}/{chance}")
    print(f"computer chose {v1}")
    print("computer won!!!")
def youu():
    print(f"{n}/{chance}")
    print(f"you chose {v1}")
    print("you won!!!")

while n<=chance :
    v1 = random.choice(list)
    v2 = str(input("Enter your choice: ")).upper()

    if v1=="SNACK" and v2=="W":
        computerr()
        com+=1
    elif v1=="SNACK" and v2=="G":
        youu()
        you+=1
    elif v1=="WATER" and v2=="G":
        computerr()
        com+=1
    elif v1=="WATER" and v2=="S":
        youu()
        you+=1
    elif v1=="GUN" and v2=="W":
        youu()
        you+=1
    elif v1=="GUN" and v2=="S":
        computerr()
        com+=1
    elif (v1=="GUN" and v2=="G") or (v1=="SNACK" and v2=="S") or (v1=="WATER" and v2=="W") : 
        print(f"{n}/{chance}")
        print(f"computer also chose {v1}")
        print("TIE!!!!")
        tie+=1
    else :
        print("Enter valid input...!")
    n+=1

print("------Game Over-----")
print(f"Number win by you {you}")
print(f"Number win by com {com}")
print(f"Number of tie {tie}")
print("\n")

if com>you :
    print("Computer is the final winner....!\n")
elif com<you :
    print("You are the final winner....!\n")
else:
    print("tie...!\n")