import os; import keyboard #so we can get events
def createScene():
    if not os.path.exists("./ScenarioBin"):
        os.makedirs("./ScenarioBin")
    newFile=open(input("Please input a name for your file: ")+".dat","x")

def createScreen(fileIn): #TODO: maybe make a program to edit text actively with x/y control and clearing w/ ANSI codes?
    if os.path.exists(fileIn):
        editFile=open(fileIn,"w")

        key=input("Area Key: ")
        print("Art (Cursor is )\n")
        art="", n=input()
        while(n!="@"):
            art=art+n+"\\n"
            n=input()
        text=input("Text: ")
        print("Choices: ")
        choices=input()

        editFile.write(key+"¦"+art+"¦"+text+"¦"+choices+"\n")

    else:
        print("ERROR: file not in directory.")
