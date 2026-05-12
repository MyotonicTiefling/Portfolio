from os import listdir; from os.path import isfile, join; from Scenario import Scenario; from Screen import Screen; import time
fileList=[file for file in listdir("./ScenarioBin") if isfile(join("./ScenarioBin",file))]

while True: 
    print("Please choose a file (Type in number and press enter):")
    print("\n".join(f"{i+1}. {choice}" for i, choice in enumerate(fileList)))
    try:
        fileind=int(input())-1
        if 0<=fileind<len(fileList):
            break
        else:
            print("INDEX OUT OF BOUNDS")
    except ValueError:
        print("NAN")

scn=Scenario("./ScenarioBin/"+fileList[fileind])
print(scn.screenDat)
active=scn.screenDat["start"]
while not (active.key[0]=="@"):
    print("\033[2J\033[H", end="") #ANSI code for clrscrn
    print(active)
    active=scn.nav(active)

print("\033[2J\033[H", end="")
active.getCompileInfo()
print(active)
time.sleep(30)