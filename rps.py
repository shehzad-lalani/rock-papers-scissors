import time
print("Made By Shehzad Karim Lalani. Visit github https://github.com/shehzad17/rock-papers-scissors to know more")
print("Version 2.0")
loose  = "The computer wins"
win = "You win"
lives = 5
computer_lives = 10
password_list = []
score = 0
drew = 0
while True:
    print("To begin,the game please fill the below information.")
    username = input("Please enter your username: ")
    password = input("Please enter password: ")
    searchFile = open("accounts.txt","r")
    for line in searchFile:
        password_list.append(line.strip())
        if username and password in password_list:
            print("Access Granted!")
            print("Welcome to Rock,Papers,Scissors")
            time.sleep(0.5)
            print("Loading.")
            time.sleep(0.5)
            print("Loading..")
            time.sleep(0.5)
            print("Loading...")
            time.sleep(0.5)
            start_menu = """
            ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
            ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
            Live Rules
            You start with" 5 lives.
            If you win you get a extra live.
            If you loose you loose a live.
            If you draw the lives stay the same.
            -----------------------------------------
            To see a list of rules type rules.
            -----------------------------------------
            At any point type exit to leave the game.
            -----------------------------------------
            The computer has lives aswell.
            Can you beat the computer?
            Good Luck!!
            -----------------------------------------
            """
            print(start_menu)
            while True:
                rps = input("Rock,Papers,Scissors?   ")
                import random
                computer = ("Rock","Papers","Scissors")
                computer = random.choice(computer)
                #rock if statments
                if rps == "Rock" and computer == "Papers":
                        print("The computer choose",computer)
                        print("")
                        print(loose)
                        print("")
                        print("")
                        lives-=1
                if rps == "Rock" and computer == "Scissors":
                        print("The computer choose",computer)
                        print("")
                        print(win)
                        print("")
                        print("")
                        score+=1
                  #paper if statements
                if rps == "Paper" and computer == "Rock":
                        print("The computer choose",computer)
                        print("")
                        print(win)
                        computer_lives -= 1
                        print("")
                        print("")
                        score+=1
                if rps == "Paper" and computer == "Scissors":
                        print("The computer choose",computer)
                        print("")
                        print(loose)
                        print("")
                        print("")
                        lives-=1
                    #scissor if statements
                if rps == "Scissors" and computer == "Papers":
                        print("The computer choose",computer)
                        print("")
                        print(win)
                        computer_lives -= 1
                        print("")
                        print("")
                        score+=1
                if rps == "Scissors" and computer == "Rock":
                        print("The computer choose",computer)
                        print("")
                        print(loose)
                        print("")
                        print("")
                        lives-=1
                    #duplicates
                if rps == "Rock" and computer == "Rock":
                        print("The computer choose",computer)
                        print("")
                        print("You Drew")
                        print("")
                        print("")
                        drew+=1
                if rps == "Paper" and computer == "Papers":
                        print("The computer choose",computer)
                        print("")
                        print("You Drew")
                        print("")
                        print("")
                        drew+=1
                if rps == "Scissors" and computer == "Scissors":
                        print("The computer choose",computer)
                        print("")
                        print("You Drew")
                        print("")
                        print("")
                        drew+=1
                    #system
                if rps == "rules":
                        print("**********************************************")
                        print("Rules")
                        print("**********************************************")
                        print("-Rock looses against Paper")
                        print("-Rock beats Scissors")
                        print("-Paper beats Rock")
                        print("-Paper looses against Scissors")
                        print("-Scissors beats Paper")
                        print("-Scissors looses against Rock")
                        print("**********************************************")
                if rps == "display lives":
                        print(lives)
                if rps == "display score":
                        print(score)
                if rps == "display drew":
                        print(drew)
                    #lives
                if lives == 0 or rps == "test":
                        print("Thanks for playing.")
                        print("You have run out of lives")
                        print("You got",score,"correct")
                        print("You drew",drew,"times")
                        stop = input("Press enter to exit.")
                        time.sleep(900)
                if computer_lives == 0:
                        print("Thanks for playing.")
                        print("The computer lost all it's lives. You Win.")
                        print("You got",score,"correct")
                        print("You drew",drew,"times")
                        stop = input("Press enter to exit.")
                        time.sleep(900)
                    #exit
                if rps == "exit":
                        break

        if password in line and password != line:
            print("Your username or password is incorrect.")
            print("---------------------------------------")
