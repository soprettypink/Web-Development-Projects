phrase = input("Input your phrase: ")
phraseNumber = int(input("How many times should it be repeated? "))
for index in range(phraseNumber):
    print((index + 1), phrase)