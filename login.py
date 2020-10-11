from tkinter import*
import os

root = Tk()
root.title("FunSmart Login Screen")

def isEmpty(str):
    return str ==""

def checkLogin():
    #global root
    #---------------------------------------------------------------
    #   Open up the username_profile.txt and verify the user credentials
    #       if the credentials match what is in file, upload user progress
    #        from file and go to main home screen
    #
    #---------------------------------------------------------------
    print(loginUsernameEntry.get())
    print(loginPasswordEntry.get())
    profileName = loginUsernameEntry.get() +"_profile.txt"

    if os.path.isfile(profileName):
        with open(profileName,"r") as file:
            temp = file.read().split(",")
            existingProfile = [content for content in temp if content.strip()]
        
        searchedUsername = existingProfile[2]
        searchedPassword = existingProfile[3]

        if(searchedUsername == loginUsernameEntry.get() and searchedPassword == loginPasswordEntry.get()):
            print("Successful Login") #remove the hard code
            # Send user to homePage
            Label(frame,text="Successful Login").grid(row=2,column=2)
            
        else:
            Label(frame,text="incorrect password").grid(row=2,column=2)
    else:
        Label(frame,text="incorrect username").grid(row=3,column=2) # remove the hard code

createProfileWindow = None
proErrorInput = None    
def submitProfile():
    #--------------------------------------------------------------------------------
    #   When user submits their profile, create a profile with the username_profile.txt
    #       store all of the acquired data in the profile
    #------------------------------------------------------------------------
    print("ready to submit")
    print("Data: " + usernameEntry.get())
    profileContent=[]
    profileContent.append(FnameEntry.get())
    profileContent.append(LnameEntry.get())
    profileContent.append(usernameEntry.get())
    profileContent.append(passwordEntry.get())
    profileContent.append(confirmPasswordEntry.get())
    profileContent.append(securityQuestion1Entry.get())
    profileContent.append(securityQuestion2Entry.get())
    #Check for completed fields
    submitNow = True
    for field in profileContent:
        if(isEmpty(field) == True):
            submitNow = False
            error = proErrorInput + "*"
            Label(createProfileWindow, text=error).grid(row=10, column=2)
            break
    #check if user profile already exist
    if(submitNow ):
        saveProfile = usernameEntry.get() + "_profile.txt" 
        if(os.path.isfile(saveProfile)):
            print("profile for "+ usernameEntry.get() + " already exist")
        else:
            print("file created")
            with open(saveProfile,"w") as file:
                for content in profileContent:
                    file.write(content + ",")
            #close profile window
            createProfileWindow.destroy()

def createProfile():
    #Lets function know you are using the global defined values
    global createProfileWindow
    global proErrorInput 
    
    #------------------------------------------------------------------------
    #   If user does not already have an account, then have user create a profile
    #       If profile already exist for the user, allow the user to reset his
    #       password
    #------------------------------------------------------------------------
    
    with open("profileMaker.txt","r") as file:
        temp = file.read().split(",")
        profileMaker = [content for content in temp if content.strip()]
    
    #Strip all the profile components from the profilemaker
    profTitle = profileMaker[0]
    profHeader = profileMaker[1]
    profFname = profileMaker[2]
    profLname = profileMaker[3]
    profUsername = profileMaker[4]
    profPassword = profileMaker[5]
    profConfirmPassword = profileMaker[6]
    profSecurityQuestionHeader = profileMaker[7]
    profSecurityQuestion1 = profileMaker[8]
    profSecurityQuestion2 = profileMaker[9]
    profSubmit = profileMaker[10]
    proErrorInput = profileMaker[11]
    
    
    createProfileWindow = Toplevel(root)
    createProfileWindow.title(profTitle)
    createProfileWindow.geometry("600x600")

    #Headers
    h1 = Label(createProfileWindow,text = profHeader)
    h1.grid(row=0,column=1)

    h2 =Label(createProfileWindow,text = profSecurityQuestionHeader)
    h2.grid(row=7,column=1)

    #Profile component label and entry
    Fname = Label(createProfileWindow, text=profFname)
    Fname.grid(row=2,column=0)
    Lname = Label(createProfileWindow, text=profLname).grid(row=3,column=0)
    username = Label(createProfileWindow, text=profUsername).grid(row=4,column=0)
    password = Label(createProfileWindow, text=profPassword).grid(row=5,column=0)
    confirmPassword = Label(createProfileWindow, text=profConfirmPassword).grid(row=6,column=0)
    securityQuestion1 = Label(createProfileWindow, text=profSecurityQuestion1).grid(row=8,column=0)
    securityQuestion2 = Label(createProfileWindow, text=profSecurityQuestion2).grid(row=9,column=0)

    Entry(createProfileWindow, textvariable=FnameEntry,width=20).grid(row=2,column=1)
    Entry(createProfileWindow, textvariable = LnameEntry, width=20).grid(row=3,column=1)
    Entry(createProfileWindow, textvariable = usernameEntry, width=20).grid(row=4,column=1)
    Entry(createProfileWindow, textvariable = passwordEntry, width=20,show="*").grid(row=5,column=1)
    Entry(createProfileWindow,textvariable = confirmPasswordEntry, width=20,show="*").grid(row=6,column=1)
    Entry(createProfileWindow, textvariable = securityQuestion1Entry, width=20).grid(row=8,column=1)
    Entry(createProfileWindow, textvariable = securityQuestion2Entry, width=20).grid(row=9,column=1)

    btn = Button(createProfileWindow,text= profSubmit, background="#263D42",command = submitProfile)
    btn.grid(row=10,column=1)

#Exterior canvas
canvas = Canvas(root, height = 600, width = 600, bg = "#263D42")
canvas.pack()

frame = Frame(root, bg="white")
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

#Username label and entry
loginUsernameLable = Label(frame, text="Username")
loginUsernameLable.grid(row=0,column=0)

loginUsernameEntry = Entry(frame, width=20)
loginUsernameEntry.grid(row=0,column=1)

#Password label and entry
loginPasswordLable = Label(frame, text="Password")
loginPasswordLable.grid(row=1,column=0)

loginPasswordEntry = Entry(frame, width=20, show="*")
loginPasswordEntry.grid(row=1,column=1)

#Login button
login = Button(frame, text="Login", bg="lightgreen", command= checkLogin)
login.grid(row=2,column=0)

#Global profile variable

var_name = StringVar()
FnameEntry = StringVar()
LnameEntry = StringVar()
usernameEntry = StringVar()
passwordEntry = StringVar()
confirmPasswordEntry =StringVar()
securityQuestion1Entry = StringVar()
securityQuestion2Entry = StringVar()

#signUp button
signUp = Button(frame, text="Sign Up", bg="lightgreen", command = createProfile)
signUp.grid(row=2,column=1)


root.mainloop()