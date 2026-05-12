from Screen import Screen; import os;
class Scenario:
    screenDat={}
    def __init__(self,fileIn): #compiles the Screens into screenDat
        self.scenarioName=os.path.basename(fileIn)
        with open(fileIn,"r",encoding="utf-8")as f:
            for line in f:
                    key,art,text,choices=line.strip().split("¦")
                    art = art.replace("\\n", "\n")
                    text = text.replace("\\n","\n")
                    if key[0]!="@": choiceDict={pair.split("#")[0]:pair.split("#")[1] for pair in choices.split("&")}
                    else: choiceDict="@"
                    self.screenDat[key]=Screen(key,art,text,choiceDict)


    def nav(self, inScr):
        while(True):
            moveTo=input("Input: ")

            if moveTo.isdigit():
                moveTo=int(moveTo)
                if moveTo>=1 and moveTo<=len(inScr.choices):
                    return self.screenDat[inScr.choices[list(inScr.choices.keys())[moveTo - 1]]]
                else: print("INDEXOUTOFBOUNDS")

            elif moveTo in inScr.choices.keys(): 
                return self.screenDat[inScr.choices[moveTo]]
                
            else: print("KEY NOT FOUND")
                    

            
    
    def getChoiceTree():
        pass