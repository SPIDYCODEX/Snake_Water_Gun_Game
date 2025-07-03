import random
while True:
 youstr=(input("Enter your choice:"))
 computer=random.choice([1,0,-1])
 Dict={"snake":1,"water":-1,"gun":0}
 you=Dict[youstr]
 Dictreverse={1:'Snake',-1:"Water",0:"Gun"}
 print(f"You choose {Dictreverse[you] } \n and computer choose:{Dictreverse[computer]}")
# now we got two value for both side: computer and Yours
 if computer==you:
    print("Match draw!")
 else:
    if computer==-1 and you==1:
        print("You Win🥂")
    elif computer==-1 and you==0:
        print("You Lose")
    
    elif computer==0 and you==1:
        print("You Lose")
    
    elif computer==0 and you==-1:
        print("You Win🥂")
    
    elif computer==1 and you==-1:
        print("You Lose")
    
    elif computer==1 and you==0:
        print("You Win🥂")
    else:
        print("something went wrong")

    
    





