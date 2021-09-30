# Designed by Austin Simpson

import random

class hangman:

    def intro(self):
        print("HANGMAN")
        print("RULES: You must enter your guess in the form of a character. Only letters A-Z. No capitals.")

    def rng(self):
        file = open("usaDictionary.txt", "r")
        data = file.read()
        words = data.split()
        num = len(words)

        rnum = random.randint(1, num)

        return rnum

    def secretWord(self, rng):
        with open('usaDictionary.txt') as f:
            lines = f.readlines()
        guess = lines[round(rng)]

        return guess

    def storeWord(self, secretWord):
        lst = list(secretWord)
        lst.pop(len(lst) - 1)

        return lst

    def checkLetter(self, lst, userGuess, turns, underScore):
        check = 0

        for i in range(len(lst)):
            if userGuess == lst[i]:
                underScore[i] = userGuess
                check += 1

        if check == 0:
            turns -= 1
            print("Sorry, there is no letter '", userGuess, "' in the word. You have ", turns, " turns left.")

        return underScore, turns

    def readData(self):
        file = open("SaveData.txt", "r")
        data = file.read()
        file.close()

        return data

    def win(self):
        data = self.readData()
        data = int(data) + 1
        print("Congratulations you have won hangman!! It took a total of ", data, " attempts on this PC.")

        file = open("SaveData.txt", "w")
        file.write('0')

        file.close()
        exit()

    def loss(self, turns):
        if turns == 0:
            data = self.readData()
            newData = int(data) + 1
            print("Sorry, you've run out of turns.. GAME OVER. You've failed to win a total of ", newData, " times.")

            file = open("SaveData.txt", "w")
            file.write(str(newData))
            file.close()

    def exe(self, turns, countUnderScore, lst,prev):
        firstUnderScore = []
        for i in range(len(lst)):
            firstUnderScore.append('_')
        UnderScore = ''.join(firstUnderScore)

        print(UnderScore)
        while turns != 0:
            userGuess = str(input("Enter your guess:"))

            match = self.prevGuess(userGuess,prev)

            if match > 0:
                self.exe(turns, countUnderScore, lst, prev)

            prev.append(userGuess)

            newLst, turns = self.checkLetter(lst, userGuess, turns, firstUnderScore)

            for i in range(len(lst)):
                if newLst[i] == '_':
                    countUnderScore += 1

            if countUnderScore == 0:
                self.win()
            else:
                countUnderScore = 0
            UnderScoreStr = ''.join(newLst)
            if turns != 0:
                print(UnderScoreStr)
            self.loss(turns)

    def prevGuess(self, userGuess, prev):
        match = 0
        for i in range(len(prev)):
            if userGuess == prev[i]:
                print("You've already guessed that letter. Please guess again.")
                match += 1

        return match

def main():
    countUnderScore = 0
    turns = 6
    prev = []

    h = hangman()

    h.intro()
    rng = h.rng()
    secretWord = h.secretWord(rng)
    lst = h.storeWord(secretWord)



    h.exe(turns, countUnderScore, lst,prev)


main()
