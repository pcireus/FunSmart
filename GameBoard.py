from tkinter import*
from tkinter import messagebox
import os
import Methods
import random
import sandbox2
from tkmacosx import Button

# ------------------------------------------------------------
# global Variables for method functionality
#  ------------------------------------------------------------ 
AllQuestionsList = None
AllAnswersList = None
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
levelFrame = None
levelLable = None
totalScore = 0
totalPercentage = 0.00
totalQuestion = 0
totalWins =0 
totalLoss =0
totalDraws =0
stageQuestionCount =0
GameLevel = 0
stageList=[]
stageNumber = 1
incorrectAnsCount =0
timeLabel = None
seconds = 30
# ------------------------------------------------------------
# This function will verify the correct answer with the answer
#   the user selects
# ------------------------------------------------------------
def checkAns(Questionframe,SelectedBtn, ExpAnswer, ActualAnswer,i, j):
    global answered
    global totalScore
    global totalPercentage
    global totalQuestion
    global buttons
    global totalWins
    global totalLoss
    global incorrectAnsCount
    global timeLabel
    global seconds

    seconds = 30
    timeLabel.destroy()
    # If answer is correct, then place mark
    if ExpAnswer == ActualAnswer:
        SelectedBtn["text"] = "X"

        totalScore+=1
        totalPercentage = float(totalScore) / float(totalQuestion)
        # check if there is a winner

        if isWinner("X"):
            totalWins+=1
            messagebox.showinfo("Information","You won!!\n On to the next level?")
            nextLevel()
        else:
            # Call in Computer move
            CPUmove()
            if isWinner("O"):
                #if computer wins, then reset stage
                totalLoss+=1
                messagebox.showinfo("Information","You lost!!\n Play again?")
                clearBoard()
                resetStage()

    elif (GameLevel == 3):
        CPUmove()
        incorrectAnsCount+=1
        if isWinner("O"):
            totalLoss+=1
            messagebox.showinfo("Information","You lost!!\n Play again?")
            clearBoard()
            resetStage()
    else:
        SelectedBtn["text"] = "O"
        incorrectAnsCount+=1
        if isWinner("O"):
            totalLoss+=1
            clearBoard()
            resetStage()
            messagebox.showinfo("Information","You lost!!\n Play again?")

    # switch answer boolean variable
    answered = False
    Questionframe.destroy()
def resetStage():
    global questionIndex
    global stageQuestionCount
    questionIndex -=stageQuestionCount
#--------------------------------
# This function traverse the gameboard 
#   and clears everything
#--------------------------------
def clearBoard():
    global buttons
    for btn in buttons:
        for slots in btn:
            slots["text"] = " "
               
# -----------------------------------------
#  This function determines whether the user 
#    will move to the next Stage or level
# ---------------------------------------   
def nextLevel():
    global GameLevel
    global stageNumber
    global subject
    global AllQuestionsList
    global AllAnswersList
    global ParsedQuestion
    global ParsedAnswer
    global levelFrame
    global levelLable
    global stageQuestionCount
    global subject
    global totalWins
    global totalLoss
    global totalDraws
    global incorrectAnsCount

    percentage = int(( totalScore / (incorrectAnsCount + totalScore)) * 100)
    report = "Subject: "+ subject +"\nAnswered correctly: "+str(totalScore) +"\nAnswered incorrectly: "+str(incorrectAnsCount)+"\nTotal wins: "+str(totalWins) +"\nTotal loses: "+ str(totalLoss)+"\nTotal draws: "+str(totalDraws)+"\nLevel percentage: "+str(percentage)+"%"

    if stageNumber < 3:
        stageNumber +=1
        
        # clear board
        clearBoard()
    elif stageNumber == 3 and GameLevel ==1:
        # print level 1 report      
        messagebox.showinfo("Information",report)

        # Change level question
        AllQuestionsList = Methods.fileSplitter("Level2Questions.txt")
        AllAnswersList = Methods.fileSplitter("Level2Answers.txt")

        # divide approprate questions and multiple choice answers
        ParsedQuestion, ParsedAnswer = Methods.getSubQuestion(str(subject),AllQuestionsList,AllAnswersList)

        #update fields
        GameLevel +=1
        stageNumber = 1
        levelLable.config(text = "Level: "+str(GameLevel))

        # clear board
        clearBoard()
    elif stageNumber == 3 and GameLevel ==2:
        # print level 2 report
        messagebox.showinfo("Information",report)

        AllQuestionsList = Methods.fileSplitter("Level3Questions.txt")
        AllAnswersList = Methods.fileSplitter("Level2Answers.txt")

        # divide approprate questions and multiple choice answers
        ParsedQuestion, ParsedAnswer = Methods.getSubQuestion(str(subject),AllQuestionsList,AllAnswersList)

        GameLevel +=1
        stageNumber = 1
        levelLable.config(text = "Level: "+str(GameLevel))

        # clear board
        clearBoard()
    elif stageNumber == 3 and GameLevel ==3:
        messagebox.showinfo("Information","Congratualations, you beat FunSmart")
        root.destroy()
        # End of Game
    stageQuestionCount =0
        
# -----------------------------------------
#  This function allows the system to makes 
#    strategic moves vs the user
# ---------------------------------------  
def CPUmove():    
    if GameLevel == 1:
        randomMove()
    elif GameLevel == 2:
        offendMove()
    elif GameLevel == 3:
        defendOffendMove()
    return

def randomMove():
    global buttons
    max = int(openSlots())
    randNumber = random.randint(1, max)

    count = 0
    for btn in buttons:
        for slots in btn:
            if slots["text"] == " ":
                count +=1
            if count == randNumber:
                slots["text"] = "O"
                return

def offendMove():
    global buttons
    # check possible win diagonal
    if buttons[0][0]["text"] == buttons[1][1]["text"] and buttons[1][1]["text"] ==  "O" and buttons[2][2]["text"] == " ":
        buttons[2][2]["text"] = "O"
        return
    elif buttons[0][2]["text"] == buttons[1][1]["text"] and buttons[1][1]["text"] == "O" and buttons[2][0]["text"] == " ":
        buttons[2][0]["text"] = "O"
        return
    elif buttons[2][2]["text"] == buttons[1][1]["text"] and buttons[1][1]["text"] == "O" and buttons[0][0]["text"] == " ":
        buttons[0][0]["text"] = "O"
        return
    elif buttons[2][0]["text"] == buttons[1][1]["text"] and buttons[1][1]["text"] == "O" and buttons[0][2]["text"] == " ":
        buttons[0][2]["text"] = "O"
        return
    elif buttons[0][0]["text"] == buttons[2][2]["text"] and buttons[2][2]["text"] == "O" and buttons[1][1]["text"] == " ":
        buttons[1][1]["text"] = "O"
        return
    elif buttons[2][0]["text"] == buttons[0][2]["text"] and buttons[0][2]["text"] == "O" and buttons[1][1]["text"] == " ":
        buttons[1][1]["text"] = "O"
        return

     # Check horizontal win
    for i in range(0,len(buttons[0])):
        count =0
        x = 0 
        y = 0
        for k in range(0,len(buttons[0])):
            if buttons[i][k]["text"] == "O":
                count +=1
            elif buttons[i][k]["text"] == " ":
                x = i
                y = k
        if count == 2:
            buttons[x][y]["text"]= "O"
            return

    # check possible win vertical
    for i in range(0,len(buttons[0])):
        count =0
        x = 0 
        y = 0
        for k in range(0,len(buttons[0])):
            if str(buttons[k][i]["text"])== "O":
                count +=1
            elif buttons[k][i]["text"] == " ":
                x = k
                y = i
        if count == 2:
            buttons[x][y]["text"] = "O"
            return
             
    randomMove()

    # else play random
def openSlots():
    global buttons
    
    count = 0
    for btn in buttons:
        for slots in btn:
            if slots["text"] == " ":
                count +=1
    return count
            
def defendOffendMove():
    global buttons
    opponent = "X"
    player = "O"
    # check possible win diagonal
    if buttons[0][0]["text"] == buttons[1][1]["text"] and buttons[1][1]["text"] ==  player and buttons[2][2]["text"] == " ":
        buttons[2][2]["text"] = "O"
        return
    elif buttons[0][2]["text"] == buttons[1][1]["text"] and buttons[1][1]["text"] == player and buttons[2][0]["text"] == " ":
        buttons[2][0]["text"] = "O"
        return
    elif buttons[2][2]["text"] == buttons[1][1]["text"] and buttons[1][1]["text"] == player and buttons[0][0]["text"] == " ":
        buttons[0][0]["text"] = "O"
        return
    elif buttons[2][0]["text"] == buttons[1][1]["text"] and buttons[1][1]["text"] == player and buttons[0][2]["text"] == " ":
        buttons[0][2]["text"] = "O"
        return
    elif buttons[0][0]["text"] == buttons[2][2]["text"] and buttons[2][2]["text"] == player and buttons[1][1]["text"] == " ":
        buttons[1][1]["text"] = "O"
        return
    elif buttons[2][0]["text"] == buttons[0][2]["text"] and buttons[0][2]["text"] == player and buttons[1][1]["text"] == " ":
        buttons[1][1]["text"] = "O"
        return

    # Check horizontal win
    for i in range(0,len(buttons[0])):
        count =0
        x = 0 
        y = 0
        for k in range(0,len(buttons[0])):
            if buttons[i][k]["text"] == player:
                count +=1
            elif buttons[i][k]["text"] == " ":
                x = i
                y = k
        if count == 2:
            buttons[x][y]["text"]= "O"
            return

    # check possible win vertical
    for i in range(0,len(buttons[0])):
        count =0
        x = 0 
        y = 0
        for k in range(0,len(buttons[0])):
            if str(buttons[k][i]["text"])== player:
                count +=1
            elif buttons[k][i]["text"] == " ":
                x = k
                y = i
        if count == 2:
            buttons[x][y]["text"] = "O"
            return

    # check possible diagonal loss
    if buttons[0][0]["text"] == buttons[1][1]["text"] and buttons[1][1]["text"] ==  opponent and buttons[2][2]["text"] == " ":
        buttons[2][2]["text"] = "O"
        return
    elif buttons[0][2]["text"] == buttons[1][1]["text"] and buttons[1][1]["text"] == opponent and buttons[2][0]["text"] == " ":
        buttons[2][0]["text"] = "O"
        return
    elif buttons[2][2]["text"] == buttons[1][1]["text"] and buttons[1][1]["text"] == opponent and buttons[0][0]["text"] == " ":
        buttons[0][0]["text"] = "O"
        return
    elif buttons[2][0]["text"] == buttons[1][1]["text"] and buttons[1][1]["text"] == opponent and buttons[0][2]["text"] == " ":
        buttons[0][2]["text"] = "O"
        return
    elif buttons[0][0]["text"] == buttons[2][2]["text"] and buttons[2][2]["text"] == opponent and buttons[1][1]["text"] == " ":
        buttons[1][1]["text"] = "O"
        return
    elif buttons[2][0]["text"] == buttons[0][2]["text"] and buttons[0][2]["text"] == opponent and buttons[1][1]["text"] == " ":
        buttons[1][1]["text"] = "O"
        return
    # Check possible horizontal loss
    for i in range(0,len(buttons[0])):
        count =0
        x = 0
        y = 0
        for k in range(0,len(buttons[0])):
            if buttons[i][k]["text"] == opponent:
                count +=1
            elif buttons[i][k]["text"] == " ":
                x = i
                y = k
        if count == 2:
            buttons[x][y]["text"]= "O"
            return

    # check possible loss vertical
    for i in range(0,len(buttons[0])):
        count =0
        x = 0
        y = 0
        for k in range(0,len(buttons[0])):
            if buttons[k][i]["text"]== opponent:
                count +=1
            elif buttons[k][i]["text"]== " ":
                x = k
                y = i
        if count == 2: 
            buttons[x][y]["text"] = "O"
            return
    randomMove()

# -----------------------------------------
# Function determines if there is a winner
# -----------------------------------------
def isWinner(token):
    global buttons
    global totalDraws
    # Check slope win
    if (str(buttons[0][0]["text"]) == str(buttons[1][1]["text"])) and (str(buttons[1][1]["text"]) == str(buttons[2][2]["text"])) and (str(buttons[2][2]["text"]) == str(token)):
        return True
    elif buttons[0][2]["text"] == buttons[1][1]["text"] and buttons[1][1]["text"] == buttons[2][0]["text"] and buttons[2][0]["text"] == str(token):
        return True
    # Check horizontal win
    count =0
    for btn in buttons:
        count =0
        for slots in btn:
            if str(slots["text"]) == str(token):
                count +=1
        if count == 3:
            return True
    # Check vertical win
    for i in range(0,len(buttons[0])):
        count =0
        for k in range(0,len(buttons[0])):
            if str(buttons[k][i]["text"])== str(token):
                count +=1
        if count == 3:
            return True
    # Check if draw
    totalDraws+=isDraw()
    return False
def isDraw():
    global buttons
    emptySlots = False
    for btn in buttons:
        for slots in btn:
            if slots["text"] == " ":
                emptySlots = True
    # print message if there is a draw and clear the baord and reset stage
    if emptySlots == False:
        clearBoard()
        resetStage()
        messagebox.showinfo("Information","Its a draw!!\n Try again?")
        return 1
    return 0
def refresh_label(frame, SelectedBtn, i,j):
    global timeLabel
    global seconds
    global Questionframe
    
    # global timeOut
    """ refresh the content of the label every second """
    # increment the time
    if seconds !=0:
        seconds -= 1
        # display the new time
        timeLabel.configure(text="%i s" % seconds)
        # request tkinter to call self.refresh after 1s (the delay is given in ms)
        timeLabel.after(1000, lambda:refresh_label(frame, SelectedBtn, i,j))
    else:
        
        # timeLabel.destroy()
        checkAns(Questionframe,SelectedBtn," ","noAnswer",i, j)
        # return True
# ------------------------------------------------------------
#  This function will print the next question from the list to the user
#    and also the multiple choice answers
# ------------------------------------------------------------
def nextQuestion(frame, SelectedBtn,i, j):
    global answered
    global Questionframe
    global ParsedQuestion
    global ParsedAnswer
    global questionIndex
    global button
    global NextFrame
    global stageNumber
    global totalQuestion
    global stageQuestionCount
    global timeLabel
    global seconds
    # global timeOut
    # check if the selected field is already played

    if answered == False and SelectedBtn["text"] == " ":
        answered = True

        # Display answer and retreive answer and check if the answer is correct
        Questionframe = Frame(frame, bg="white")
        Questionframe.pack(side="top", fill="x")

        Question = Label(Questionframe, text= "Stage: "+str(stageNumber) +" " + ParsedQuestion[questionIndex])
        Question.grid(row=0, column = 0)
        
        #multiple Choice list for user answers
        multChoices =[str(ParsedAnswer[questionIndex][0]), str(ParsedAnswer[questionIndex][1]),str(ParsedAnswer[questionIndex][2]), str(ParsedAnswer[questionIndex][3])]
        # identify the correct answer from the list
        correctAns = ParsedAnswer[questionIndex][0]
        # Shuffle entire list
        random.shuffle(multChoices)
        questionIndex +=1
        stageQuestionCount+=1

        totalQuestion+=1
        multChoice1 = Button(Questionframe, text = multChoices[0], command = lambda:checkAns(Questionframe,SelectedBtn,correctAns,multChoices[0],i, j))
        multChoice2 = Button(Questionframe, text = multChoices[1], command = lambda:checkAns(Questionframe,SelectedBtn,correctAns,multChoices[1],i, j))
        multChoice3 = Button(Questionframe, text = multChoices[2], command = lambda:checkAns(Questionframe,SelectedBtn,correctAns,multChoices[2],i, j))
        multChoice4 = Button(Questionframe, text = multChoices[3], command = lambda:checkAns(Questionframe,SelectedBtn,correctAns,multChoices[3],i, j))

        multChoice1.grid(row=1, column = 0, sticky=W)
        multChoice2.grid(row=1, column = 1, sticky=W)
        multChoice3.grid(row=2, column = 0, sticky=W)
        multChoice4.grid(row=2, column = 1, sticky=W)

        # Call timer
        # seconds = 5
        timeOut = False
        # label displaying time
        timeLabel = Label(frame, text="30 s", font="Arial 30", width=10)
        timeLabel.pack()
        # start the timer
        timeLabel.after(1000, lambda:refresh_label(frame, SelectedBtn,i,j))



def main(root, frame, percentage, Subject):
    root.geometry("850x560") 
    #Close pre-test screen
    global buttons
    global ParsedQuestion
    global ParsedAnswer
    global AllQuestionsList
    global AllAnswersList
    global stageNumber
    global GameLevel
    global levelLable
    global subject

    subject = Subject
    frame.destroy()
    root.title("FunSmart Gameboard Screen")
    frame = Frame(root, bg="white")
    frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)
   
    Boardframe = Frame(frame, bg="white")
    Boardframe.pack(side="bottom", fill="x")
 
    levelFrame = Frame(frame, bg="white")
    levelFrame.pack(side="left", fill="x")

    Boardframe2 = Frame(Boardframe, bg="white")
    Boardframe2.pack()
    
    #----------------------------------------------------
    # Select Level questions and answers based on percentage
    # Level1: 0% <= percentage <= 70% 
    # Level2: 70% < percentage< 90%
    # Level3: 90% <= percentage <= 100%
    #----------------------------------------------------
    if percentage <= 70:
        AllQuestionsList = Methods.fileSplitter("Level1Questions.txt")
        AllAnswersList = Methods.fileSplitter("Level1Answers.txt")
        GameLevel = 1

    elif percentage <=90:
        AllQuestionsList = Methods.fileSplitter("Level2Questions.txt")
        AllAnswersList = Methods.fileSplitter("Level2Answers.txt")
        GameLevel = 2

    elif percentage <=100:
        AllQuestionsList = Methods.fileSplitter("Level3Questions.txt")
        AllAnswersList = Methods.fileSplitter("Level3Answers.txt")
        GameLevel = 3
    levelLable = Label(levelFrame, text="Level: "+str(GameLevel))
    levelLable.pack()
    
    # divide approprate questions and multiple choice answers
    ParsedQuestion, ParsedAnswer = Methods.getSubQuestion(str(subject),AllQuestionsList,AllAnswersList)

    #----------------------------------------------------
    # Create Gameboard with a 2D 3x3 matrix as buttons
    # and add them to the Gameboard frame
    #----------------------------------------------------
    buttons=  [[0 for x in range(3)] for x in range(3)] 
    for i in range(3):
        for j in range(3):
            buttons[i][j] = Button(Boardframe2, text=" ",padx = 30, pady=30, bg="lightgrey")

            buttons[i][j].config(command=lambda SelectedBtn=buttons[i][j],x=i,y=j:nextQuestion(frame, SelectedBtn, x, y))
            buttons[i][j].grid(row=i, column=j)