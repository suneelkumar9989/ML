import random
from datetime import datetime
#Greet function to greet the user
def greet():
    print("Hey buddy I am Bot. Your Good Name Please: ",end="")
    name=input()
    time = datetime.now()
    print()
    if time.hour > 0 and time.hour < 12:
        print("Hey Good Morning",name.capitalize(),"glad to meet you")
    elif time.hour >12 and time.hour < 16:
        print("Hey Good After Noon",name.capitalize(),"glad to meet you")
    else:
        print("Hey Good Evening",name.capitalize(),"glad to meet you")
    print()
    return name
#Time function to know the time
def time():
    timenow = datetime.now()
    print()
    print("TIME : ",timenow.hour,":",timenow.minute,":",timenow.second,sep="")
    print()
#Evaluator function to ivaluate an expression
def evaluate():
    print()
    expression = input()
    print()
    print("The OUTPUT for the given expression is:",eval(expression),sep="")
    print()
#game function to play a GAME
def game(player):
    user,bot=0,0
    end = True
    while end:
        print(player.capitalize(),":",user,"  Bot:",bot,sep="")
        print()
        print("Choose\n1.ROCK\n2.PAPER\n3.SCISSORS\n4.END GAME")
        choose_number = int(input())
        if choose_number>4:
            print("Please enter value between 1-4\n")
            continue
        if choose_number == 4:
            end = False
            print()
            if user>bot:
                print(player.capitalize(),"WON")
            elif user<bot:
                print("Bot WON")
            else:
                print("DRAW")
            print()
            break
        list_of_items=["rock","paper","scissors"]
        choice = list_of_items[choose_number-1]
        output = random.choice(list_of_items)
        if output == choice:
            print("Oh its a DRAW")
        if output=="rock":
            if choice == "paper":
                print("Hurray YOU WIN it is",output)
                user+=1
            elif choice == "scissors":
                print("Oops YOU LOSE it is",output)
                bot+=1
        if output=="scissors":
            if choice == "paper":
                print("Oops YOU LOSE it is",output)
                bot+=1
            elif choice == "rock":
                print("Hurray YOU WIN it is",output)
                user+=1
        if output=="paper":
            if choice == "scissors":
                print("Hurray YOU WIN it is",output)
                user+=1
            elif choice == "rock":
                print("Oops YOU LOSE it is",output)
                bot+=1
        print()
#Actions that are done by BOT
def bot():
    name=greet()
    quit = True
    while quit:
        #list of tasks done by bot
        print("How can I help you\npress 1 to know TIME\npress 2 to evaluate an expression\npress 3 to play a Game\npress 4 to Quit\n")
        action = int(input())
        if action>4:
            print("Please enter value between 1-4\n")
            continue
        if(action == 1):
            time()
        elif action == 2:
            evaluate()
        elif action == 3:
            game(name)
        else: 
            quit = False
bot()
#Thanking to quit BOT
print("I am glad that I am a bit helpful for you.I am still in developing stage.Thank you :)")