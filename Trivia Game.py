
import random


class Question():
    triviaquestion = ""
    def __init__(self, triviaquestion, answer1, answer2, answer3, answer4, correctanswer):
        self.triviaquestion = triviaquestion
        self.answers = [answer1, answer2, answer3, answer4]
        self.correctanswer = correctanswer
    def getAnswer(self, index):
        return self.answers[index]
        
qSet = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

def askQuestion(trquestions):
        for x in qSet:
            r = random.randint(1,10)
            print("x:",x,"r:",r)
            if (x == r):
                qSet.remove(r)
                break
        q = trquestions[r-1]
        print(q.triviaquestion)
        ord = 1
        for a in q.answers:
            print(ord, ":" , a)
            ord = ord + 1
        return q

def checkAnswer(q, ans):
        print(q.getAnswer(ans-1))
        if (ans == q.correctanswer):
            print("Success")
            return 1
        else: 
            print("False")
            return 0


def main():
    trquestions = []
    trquestions.append(Question("Bir bir daha kaç eder?", "1", "2", "3", "4", 2))
    trquestions.append(Question("iki kere iki  kaç eder?", "1", "2", "3", "4", 4))
    trquestions.append(Question("üç üç daha kaç eder?", "6", "2", "3", "4", 1))
    trquestions.append(Question("dört dört daha kaç eder?", "12", "16", "8", "2", 3))
    trquestions.append(Question("beş beş daha kaç eder?", "10", "20", "30", "40", 1))
    trquestions.append(Question("altı altı daha kaç eder?", "11", "12", "13", "14", 2))
    trquestions.append(Question("yedi yedi daha kaç eder?", "15", "21", "31", "14", 4))
    trquestions.append(Question("sekiz sekiz daha kaç eder?", "16", "24", "32", "40", 1))
    trquestions.append(Question("dokuz dokuz daha kaç eder?", "18", "22", "32", "49", 1))
    trquestions.append(Question("on kere on kaç eder?", "10", "20", "30", "100", 4))

    playerOneScore = 0
    playerTwoScore = 0

    for qc in range(1,5):
        print("Player1 it's your turn")
        q = askQuestion(trquestions)
        ans = int(input("What's your answer? "))
        playerOneScore = playerOneScore + checkAnswer(q, ans)
        print("Player2 it's your turn")
        q = askQuestion(trquestions)
        ans = int(input("What's your answer? "))
        playerTwoScore = playerTwoScore + checkAnswer(q, ans)
        print("Player1: ", playerOneScore, " Player2: ", playerTwoScore)

    print(playerOneScore, playerTwoScore)
    if (playerOneScore > playerTwoScore):
        print("Player1 is the winner")
    elif (playerOneScore < playerTwoScore):
        print("Player2 is the winner")
    elif (playerOneScore == playerTwoScore):
        print("Drawback")

main()