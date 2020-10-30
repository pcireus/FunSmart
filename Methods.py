#Given a filename, this method opens the file and read and return a string splitting the method by a comma
def fileSplitter(profileName):
    
    with open(profileName,"r") as file:
        temp = file.read().split(",")
        existingProfile = [content for content in temp if content.strip()]
    return existingProfile
def isEmpty(str):
    return str ==""
