#Given a filename, this method opens the file and read and return a string splitting the method by a comma
def fileSplitter(profileName):
    
    with open(profileName,mode ="r",encoding='utf-8-sig') as file:
        temp = file.read().split(",")
        existingProfile = [content.replace("\n", "").strip() for content in temp]
    return existingProfile

def isEmpty(str):
    return str ==""
# ---------------------------------------------------------------------
# This method will parse out the question based on the subjects
# Science range (1 - 30)
# Math range (31 - 60)
# History range (61 - 90)
# All subjects range (91 - 120)
# ---------------------------------------------------------------------
def getSubQuestion(subject,AllQuestionsList,AllAnswersList):
    print("innnnn: "+subject)
    start =0
    end = 4
    # if subject == "All subjects":
    #             print("5kdkdkdkdkdkdkdkdkdkdkdkdkdkdkdkdkdkdkdkdkdkdkdkdkdkdkdkdkdkd")
    if subject == "Science":
        questionList = AllQuestionsList[:30]
        answerList = AllAnswersList[0:120]
        return getMultChoice(questionList, start, end, answerList)
    elif subject == "Math":
        questionList = AllQuestionsList[30:60]
        answerList = AllAnswersList[120:240]
        return getMultChoice(questionList, start, end, answerList)
    elif subject == "History":
        questionList = AllQuestionsList[60:90]
        answerList = AllAnswersList[240:360]
        return getMultChoice(questionList, start, end, answerList)
    elif subject == "All subject":
        questionList = AllQuestionsList[90:120]
        answerList = AllAnswersList[360:480]
        return getMultChoice(questionList, start, end, answerList)

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