
class Question():
    triviaquestion = ""
    def __init__(self, triviaquestion, answer1, answer2, answer3, answer4, correctanswer):
        self.triviaquestion = triviaquestion
        self.answers = [answer1, answer2, answer3, answer4]
        self.correctanswer = correctanswer
    def getAnswer(self, index):
        return self.answers[index]
        
    
# trquestions = Question[10]
# trquestions[0] = Question("Bir bir daha kaç eder?", "1", "2", "3", "4", 2)
# trquestions[1] = Question("iki kere iki  kaç eder?", "1", "2", "3", "4", )
# trquestions[2] = Question("Bir bir daha kaç eder?", "1", "2", "3", "4", 2)
# trquestions[3] = Question("Bir bir daha kaç eder?", "1", "2", "3", "4", 2)
# trquestions[4] = Question("Bir bir daha kaç eder?", "1", "2", "3", "4", 2)
# trquestions[5] = Question("Bir bir daha kaç eder?", "1", "2", "3", "4", 2)
# trquestions[6] = Question("Bir bir daha kaç eder?", "1", "2", "3", "4", 2)
# trquestions[7] = Question("Bir bir daha kaç eder?", "1", "2", "3", "4", 2)
# trquestions[8] = Question("Bir bir daha kaç eder?", "1", "2", "3", "4", 2)
# trquestions[9] = Question("Bir bir daha kaç eder?", "1", "2", "3", "4", 2)

def main():
    trquestions = Question[10]
    trquestions[0] = Question("Bir bir daha kaç eder?", "1", "2", "3", "4", 2)
    trquestions[1] = Question("iki kere iki  kaç eder?", "1", "2", "3", "4", 4)
    trquestions[2] = Question("Bir bir daha kaç eder?", "1", "2", "3", "4", 2)
    trquestions[3] = Question("Bir bir daha kaç eder?", "1", "2", "3", "4", 2)
    trquestions[4] = Question("Bir bir daha kaç eder?", "1", "2", "3", "4", 2)
    trquestions[5] = Question("Bir bir daha kaç eder?", "1", "2", "3", "4", 2)
    trquestions[6] = Question("Bir bir daha kaç eder?", "1", "2", "3", "4", 2)
    trquestions[7] = Question("Bir bir daha kaç eder?", "1", "2", "3", "4", 2)
    trquestions[8] = Question("Bir bir daha kaç eder?", "1", "2", "3", "4", 2)
    trquestions[9] = Question("Bir bir daha kaç eder?", "1", "2", "3", "4", 2)

    for q in trquestions:
        print(q)
