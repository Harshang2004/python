# time
import datetime
def gettime():
    return datetime.datetime.now()
print("-----------Health Management Program---------\n")
print("Press 1 for Harshang\nPress 2 for Devam\nPress 3 for Harv\n")
person = int(input("->"))
print("Press 1 for Exercise\nPress 2 for Food\n")
exefood = int(input("->"))
print("Press 1 to add data\nPress 2 to get data\n")
addget = int(input("->"))
if person==1:
    if exefood==1 and addget==1:
        value = input("Enter Exercise name\n->")
        with open("harshang_exe.txt","a") as harshang_exe:
            harshang_exe.write(str([str(gettime())])+": "+value+"\n")
        print("successfully written")
    elif exefood==2 and addget==1:
        value = input("Enter food name\n->")
        with open("harshang_food.txt","a") as harshang_food:
            harshang_food.write(str([str(gettime())])+": "+value+"\n")
        print("successfully written")
    elif exefood==1 and addget==2:
        with open("harshang_exe.txt") as harshang_exe:
            for x in harshang_exe:
                print(x, end="")
    elif exefood==2 and addget==2:
        with open("harshang_food.txt") as harshang_food:
            for x in harshang_food:
                print(x, end="")
    else:
        print("enter valid input!!!")
elif person==2:
    if exefood==1 and addget==1:
        value = input("Enter Exercise name\n->")
        with open("devam_exe.txt","a") as devam_exe:
            devam_exe.write(str([str(gettime())])+": "+value+"\n")
        print("successfully written")
    elif exefood==2 and addget==1:
        value = input("Enter food name\n->")
        with open("devam_food.txt","a") as devam_food:
            devam_food.write(str([str(gettime())])+": "+value+"\n")
        print("successfully written")
    elif exefood==1 and addget==2:
        with open("devam_exe.txt") as devam_exe:
            for x in devam_exe:
                print(x, end="")
    elif exefood==2 and addget==2:
        with open("devam_food.txt") as devam_food:
            for x in devam_food:
                print(x, end="")
    else:
        print("enter valid input!!!")
elif person==3:
    if exefood==1 and addget==1:
        value = input("Enter Exercise name\n->")
        with open("harv_exe.txt","a") as harv_exe:
            harv_exe.write(str([str(gettime())])+": "+value+"\n")
        print("successfully written")
    elif exefood==2 and addget==1:
        value = input("Enter food name\n->")
        with open("harv_food.txt","a") as harv_food:
            harv_food.write(str([str(gettime())])+": "+value+"\n")
        print("successfully written")
    elif exefood==1 and addget==2:
        with open("harv_exe.txt") as harv_exe:
            for x in harv_exe:
                print(x, end="")
    elif exefood==2 and addget==2:
        with open("harv_food.txt") as harv_food:
            for x in harv_food:
                print(x, end="")
    else:
        print("enter valid input!!!")
else: 
    print("enter valid input!!!")