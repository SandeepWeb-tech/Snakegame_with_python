import random

def game(comp,you):
    if comp == you:
        return None
    if comp == 's':
        if you == 'w':
            return False
        elif you == 'g':
            return True
    if comp == 'w':
        if you == 'g':
            return False
        elif you == 's':
            return True
    if comp == 'g':
        if you == 's':
            return False
        elif you == 'w':
            return True
        
        

print("Comp : Snake(s) water(w) or gun(g)? ")
randNo = random.randint(1,3)
if randNo == 1:
    comp = 's'
elif randNo ==2:
    comp ='w'
else:
    comp ='g'



you = input(" You : Snake(s) water(w) or gun(g)?")

print(f"comp choose {comp}")
a = game(comp,you)

if a == None:
    print("Tie")
elif a:
    print("You Win")
else:
    print("You Lose")


