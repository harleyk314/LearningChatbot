#Required Updates:
    #
    #Should only search messsages written by person.
    #


#Here are some constants we shall use.
NEWLINE = "¿"
PERSON_TALKS = "Ä"
BOT_TALKS = "Ö"

#The person speaks first
#watch out for mutability issues

print("Say hi to Chatbot!")
print()
conversation = PERSON_TALKS

#Loop forever (we can change this later)
while(True):

    #Ask user to enter their message

    print("You: ", end = '')
    
    newMessage = input()
    conversation += newMessage

    print()

    #Now the bot is speaking
    conversation += BOT_TALKS
    print("Bot: ", end = '')

    #print(conversation)

    #Let's generate ChatBot's message:

    #Keep generating letters until it decides to stop, basically.
    for letter in range(100):
        highScore = 0
        bestLetter = "NULL"
        length = len(conversation)
        for i in range(length):
            #if we've been searching for too long, exit the loop. We're done.
            if (i >= length - 1):
                break

            score = 0
            for j in range(i + 1):
                currentLetter = conversation[i-j]
                #print(length)
                #print(i)
                #print(j)
                #print()
                comparedLetter = conversation[length - 1 - j]

                #Read in reverse (i.e. interpret the person as the bot and vice versa)
                if currentLetter == PERSON_TALKS:
                    currentLetter = BOT_TALKS
                elif currentLetter == BOT_TALKS:
                    currentLetter = PERSON_TALKS

                #print("Current = " + currentLetter)
                #print("Compared = " + comparedLetter)
                if currentLetter != comparedLetter:
                    #stop this search
                    break
                #else:
                    #print("good")
                    #print(currentLetter)

                score += 1
                #print(score)

            if score >= highScore:
                highScore = score
                bestLetter = conversation[i + 1]
        if bestLetter == "NULL":
            print("ERROR")
            break
        else:
            if bestLetter == PERSON_TALKS or bestLetter == BOT_TALKS:
                break
            else:
                print(bestLetter, end = '')
                conversation += bestLetter
                #print("Highscore = " + str(highScore))
        
        

        #once this happens, the bot is done talking.


    print()
    print()
    conversation += PERSON_TALKS
        








