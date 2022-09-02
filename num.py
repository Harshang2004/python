print("-------------------------------------------------------------------------------------")
n = 77
print("you have 5 chances to guesse")
c = 1
while c < 9:
    g = int(input("guesses the number (1-100): \n >>>"))
    if g>n : 
        print("dicrease the number")
    elif g<n :
        print("increase the number")
    else :
        print("you won the game!!!!")
        print(c, "no of chances you took")
    c=c+1
if c==9 :
    print("game overr!!")