import random
# random library imported to generate random values

colorList = ['r','o','y','g','b','i','v', 'p', 'w', 'm']
#(2. use of lists) List of 10 colors

correctColourPlace = 0
correctColour = 0
attempt = 0
userList = []
newList = []
randList = []
wrongPlaceList = []
#variables and lists defined

def validate(a):
    if a != 'r' and a != 'o' and a != 'y' and a != 'g' and a != 'b' and a != 'i' and a != 'v' and a != 'p' and a != 'w' and a != 'm':
        print("Please enter an appropriate response and try again.")
        return 1
    else:
        return 0
#(4,6. use of logical operator and user-defined function) Error validation in the events where the user enter the unexpected values
        

randList = [ colorList[random.randint(0,9)], colorList[random.randint(0,9)], colorList[random.randint(0,9)], colorList[random.randint(0,9)] ]
#(3. use of random choice from a list) Colors are randomly chosen by the computer: 
# Numbers are randomly chosen as index for the list 'colorList' to acquire different colors

print("Welcome to the game of...")
print(" ___ ___   ____  _____ ______    ___  ____   ___ ___  ____  ____   ___   \n|   |   | /    |/ ___/|      |  /  _]|    \ |   |   ||    ||    \ |   \  \n| _   _ ||  o  (   \_ |      | /  [_ |  D  )| _   _ | |  | |  _  ||    \ \n|  \_/  ||     |\__  ||_|  |_||    _]|    / |  \_/  | |  | |  |  ||  D  |\n|   |   ||  _  |/  \ |  |  |  |   [_ |    \ |   |   | |  | |  |  ||     |\n|   |   ||  |  |\    |  |  |  |     ||  .  \|   |   | |  | |  |  ||     |\n|___|___||__|__| \___|  |__|  |_____||__|\_||___|___||____||__|__||_____| !!!\n")
#wordart with the title "Mastermind"
print("Guess the four colours randomly generated by the computer, in the CORRECT order.")
print("List of colors available: Red, Orange, Yellow, Green, Blue, Indigo, Violet, Pink, White, Magenta")
print("Note: Please use the first letter of the colour during entry. e.g.: Pink(P), White(W)\n\n")
print(randList)
#welcome message and instructions displayed to user upon program running

while correctColourPlace != 4:
    correctColourPlace = 0

    for x in range(4):
        userList.append(input("Guess the color #"+str(x+1)+ ": ").lower())
        while validate(userList[x]):
            del userList[-1]
            userList.append(input("Guess the color #"+str(x+1)+": ").lower())
    #(1. use of input data) 4 guesses of color is requested from user in sequence, lower() is used to decapitalize every character for comparisons
    #(4. use of if statements and relational operators) The if statements are used as error validation

    for y in range(4):
        if userList[y] == randList[y]:
            correctColourPlace += 1
        else:
            for r in range(4):
                if randList[y] == userList[r]:
                    correctColour += 1
                    userList[r]= 'x'
    #for loop for counters of correct color&place & correct color (not place)

    print("\nCorrect colour in the correct place: ", str(correctColourPlace), "\nCorrect colour but in the wrong place: ", str(correctColour))
    #???1. use of display data)

    if correctColourPlace != 4:
        print("Please try again, you can do it! :)\n")
    #Prompt user to retry the game
    
    attempt += 1
    #counter for number of user attempts
    userList.clear()
    wrongPlaceList.clear()
    newList.clear()
    correctColour = 0
    #clears the data of the variables and lists for new attempts to be made
#(5. use of loops)

print("\nCongratulations! You have won the Mastermind game! No candies for you, but I'm still happy for your win. :)")
print("The answer: ")
print("| ", end="")
for z in range(4):
    print(randList[z], end=" | ")
print("\nYou have attempted ", str(attempt), "times in total. Aim higher next time!" )
#Complete ending message for user who have won the game with the message itself, the answer and number of attempts made