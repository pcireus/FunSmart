from tkinter import*
import os
import GameBoard
import Methods
import random
from tkinter import messagebox
# --------------------------
# Global Variables
# --------------------------
AllQuestionsList = Methods.fileSplitter("PreTestQuestions.txt")
AllAnswersList = Methods.fileSplitter("PreTestAnswers.txt")
ParsedQuestion =[]
ParsedAnswer = []
questionIndex = 0
answered = False
tempAns = ""
isLastQuestion = False
NextFrame = None
button = None
Questionframe = None
root = None
totalScore = 0
totalPercentage = 0.00
totalQuestion = 10
statusBar = None

#---------------------------------------------------------------------
# This function checks for correct answers
#---------------------------------------------------------------------
def checkAns(frame, ExpAnswer, ActAnswer):
    global answered
    global totalScore
    global totalPercentage
    global totalQuestion
    # Calculate User percentage
    if ExpAnswer == ActAnswer:
        totalScore +=1

    # switch answer boolean variable
    answered = False

def placement(frame, subject):
    totalPercentage = int((totalScore / totalQuestion) * 100)
    messagebox.showinfo("Information",str(subject) + " pre test is complete\n Grade = "+str(totalPercentage)+"%")
    GameBoard.main(root, frame, totalPercentage, subject)

# ------------------------------------------------------------
#  This function will print the next question from the list to the user
#    and also the multiple choice answers
# ------------------------------------------------------------
def nextQuestion(frame,subject):
    global answered
    global Questionframe
    global ParsedQuestion
    global ParsedAnswer
    global questionIndex
    global button
    global NextFrame
    global statusBar

    # Display answer and retreive answer and check if the answer is correct
    if answered == False:
        answered = True
        Questionframe.destroy()

        Questionframe = Frame(frame, bg="white")
        Questionframe.pack(side="top", fill="x")
    
        Question = Label(Questionframe, text= ParsedQuestion[questionIndex])
        Question.grid(row=0, column = 0)
        
        tempIndex = questionIndex + 1
        statusBar.config(text= str(tempIndex)+" - "+ str(totalQuestion))
       
        #multiple Choice list for user answers
        multChoices =[str(ParsedAnswer[questionIndex][0]), str(ParsedAnswer[questionIndex][1]),str(ParsedAnswer[questionIndex][2]), str(ParsedAnswer[questionIndex][3])]

        # identify the correct answer from the list
        correctAns = ParsedAnswer[questionIndex][0]
        # Shuffle entire list
        random.shuffle(multChoices)
        # Display list to user
        v = StringVar()

        Radiobutton(Questionframe, text = multChoices[0],variable=v, value="answer1",command=lambda:checkAns(frame, correctAns, multChoices[0])).grid(row=1, column = 0)
        Radiobutton(Questionframe, text = multChoices[1],variable=v, value="answer2",command=lambda:checkAns(frame, correctAns, multChoices[1])).grid(row=1, column = 1)
        Radiobutton(Questionframe, text = multChoices[2],variable=v, value="answer3",command=lambda:checkAns(frame, correctAns, multChoices[2])).grid(row=2, column = 0)
        Radiobutton(Questionframe, text = multChoices[3],variable=v, value="answer4",command=lambda:checkAns(frame, correctAns, multChoices[3])).grid(row=2, column = 1)
    
        #increment quesiton list until 10th increment
        if questionIndex < 9:
            questionIndex +=1      
         # enable the submit button
        else:
            
            button.destroy()
            button = Button(NextFrame, text="Submit",command = lambda:placement(frame,subject))
            button.pack(anchor = E)
    return
# ---------------------------------------------------------------------
# This method will parse out the question based on the subjects
# Science range (1 - 10)
# Math range (11 - 20)
# History range (21 - 30)
# All subject range ( 31 - 60)
# ---------------------------------------------------------------------
def getSubQuestion(subject):

    start =0
    end = 4
    if subject == "Science":
        questionList = AllQuestionsList[:10]
        answerList = AllAnswersList[:41]    
        return getMultChoice(questionList, start, end, answerList)
    
    elif subject == "Math":
        questionList = AllQuestionsList[10:20]
        answerList = AllAnswersList[41:81]
        return getMultChoice(questionList, start, end, answerList)

    elif subject == "History":
        questionList = AllQuestionsList[20:30]
        answerList = AllAnswersList[81:121]
        return getMultChoice(questionList, start, end, answerList)
    
    elif subject == "All subjects":
        questionList = AllQuestionsList[30:60]
        answerList = AllAnswersList[121:161]
        return getMultChoice(questionList, start, end, answerList)

#---------------------------------------------------------------------
# This function gets the multiple choice answers from the file
#---------------------------------------------------------------------
def getMultChoice(questionList, answerStart, answerEnd, answerList):
    multipleChoice = []
    for question in questionList:
        tempList = []
        for answer in range(answerStart,answerEnd):
            tempList.append(answerList[answer])

        answerStart = answerEnd
        answerEnd+=4
        multipleChoice.append(tempList)
    return questionList, multipleChoice
#---------------------------------------------------------------------
# Main driver method
#---------------------------------------------------------------------
def main(Root, frame, subject):

    global Questionframe
    global ParsedQuestion
    global ParsedAnswer
    global button
    global NextFrame
    global root
    global statusBar
    global totalQuestion

    root = Root

    #divide approprate questions and multiple choice answers
    ParsedQuestion, ParsedAnswer = getSubQuestion(str(subject))

    frame.destroy()
    root.title("FunSmart " + str(subject) +" Prestest Screen")

    # create new frame that will replace the previous one
    frame = Frame(root, bg="white")
    frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

    # create question frames storing only next question button
    Questionframe = Frame(frame, bg="white")
    Questionframe.pack(side="top", fill="x")

    NextFrame = Frame(frame, bg="white")
    NextFrame.pack(side="bottom", fill="x")

    Question = Label(Questionframe, text= "Welcome to the "+str(subject) + " pre-test, please click 'Next Question' to continue")
    Question.grid(row=0, column = 0)

    statusBar = Label(NextFrame, text=str(questionIndex)+" - "+str(totalQuestion))
    statusBar.pack(anchor = W)
    
    button = Button(NextFrame, text=" Next Question ",command = lambda:nextQuestion(frame, subject))
    button.pack(anchor = E)