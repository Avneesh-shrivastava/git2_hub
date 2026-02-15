import random

list = ["Consistency beats motivation.","You don’t get fit by wishing. You get fit by working.","Small progress every day adds up to big results.",
                   "Discipline is choosing what you want most over what you want now.",
                   "Your future body is built by today’s choices.",
                   "Work in silence. Let results make the noise."]

i = 1
while i <= len(list):
    c = random.choice(list)
    
    put = input("Press enter to get motivated!")
    if put == "":
        print("\n",c,"\n")
    else:
        print("I think you don't want to get motivated")
    i = i + 1    