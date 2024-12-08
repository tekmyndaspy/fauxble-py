import os
import sys
import random
import subprocess

print("Starting Fauxble.")

# User definable variables
mainVideoDir='Main' # Defines the folder which contains main videos. Default is 'Main'.
intermediaryVideoDir='Intermediary' # Defines the folder which contains intermediary videos. Default is 'Intermediary'.
allowedExtensions = ['.mp4', '.webm'] # Defines the list of extensions accepted by the videoplayer.
videoPlayer = 'mpv --fs --af=loudnorm' # Defines the videoplayer and commandline arguments for playing videos.

# Important constants that the script uses. Don't touch these, unless you know what you're doing.
scriptRoot = os.path.dirname(os.path.realpath(sys.argv[0]))

# main fauxble loop.
# TODO: find a cleaner way to have fauxble loop forever without using a while true loop (is that actually an issue?)
while (True):
    # select random file directly in, or in a subfolder of, the main video directory
    print("")
    print("Choosing main video.")
    os.chdir(scriptRoot)
    os.chdir(mainVideoDir)
    fileNotChosen = True
    while fileNotChosen:
        # create list of files in the current working directory
        files = os.listdir()
        
        # if the working directory doesn't have any items, return to main video directory and restart loop
        if not files:
            print("No items found in " + os.getcwd() + ". Returning to " + mainVideoDir + ".")
            os.chdir(scriptRoot)
            os.chdir(mainVideoDir)
            continue
        
        # select random item in working directory for review
        potentialItem = random.choice(files)
        
        # if the item is a directory, enter the directory, and restart the loop
        if os.path.isdir(potentialItem):
            print("Entering " + potentialItem + ".")
            os.chdir(potentialItem)
            continue
        
        # if the item is a file, check if extension is in allowed list. 
        # if it is not, return to main video directory, and restart loop.
        if os.path.isfile(potentialItem):
            if os.path.splitext(potentialItem)[-1].lower() not in allowedExtensions:
                print(potentialItem + " extension not in allowedExtensions.")
                os.chdir(scriptRoot)
                os.chdir(mainVideoDir)
                continue
            print(potentialItem + " chosen.")
            chosenFile = potentialItem
            fileNotChosen = False
            
    # play the chosen file.
    print("Playing" + chosenFile + ".")
    subprocess.run(videoPlayer + " \"" + chosenFile + "\"")

    # select random file directly in, or in a subfolder of, the intermediary video directory
    print("")
    print("Choosing intermediary video.")
    os.chdir(scriptRoot)
    os.chdir(intermediaryVideoDir)
    fileNotChosen = True
    while fileNotChosen:
        # create list of files in the current working directory
        files = os.listdir()
        
        # if the working directory doesn't have any items, return to main video directory and restart loop
        if not files:
            print("No items found in " + os.getcwd() + ".")
            os.chdir(scriptRoot)
            os.chdir(intermediaryVideoDir)
            continue
        
        # select random item in working directory for review
        potentialItem = random.choice(files)
        
        # if the item is a directory, enter the directory, and restart the loop
        if os.path.isdir(potentialItem):
            print("Entering " + potentialItem + ".")
            os.chdir(potentialItem)
            continue
        
        # if the item is a file, check if extension is in allowed list. 
        # if it is not, return to main video directory, and restart loop.
        if os.path.isfile(potentialItem):
            if os.path.splitext(potentialItem)[-1].lower() not in allowedExtensions:
                print(potentialItem + " extension not in allowedExtensions.")
                os.chdir(scriptRoot)
                os.chdir(intermediaryVideoDir)
                continue
            print(potentialItem + " chosen.")
            chosenFile = potentialItem
            fileNotChosen = False
            
    # play the chosen file.
    print("Playing" + chosenFile + ".")
    subprocess.run(videoPlayer + " \"" + chosenFile + "\"")