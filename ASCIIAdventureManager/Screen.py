class Screen:
    def __init__(self,key,art,text,choices):
        self.key=key #screen key
        self.art=art #ascii art
        self.text=text #screen text
        self.choices=choices #choices dict, leading to other screens
    
    def __str__(self):
        if self.key[0]!="@": result= "\n".join(f"{i+1}. {choice}" for i,choice in enumerate(self.choices.keys()))
        else: result=""
        return f"+==========+\n{self.art}\n{self.text}\n\n{result}\n+==========+\n\n"
    
    def getCompileInfo(self):
            print(f"Screen Info\n\tName: {self.key}\n\tChoices:")
            if self.key[0]!="@":
                for k in self.choices:
                    print(f"\t\t{k} -> {self.choices[k]}")
            else:
                print("\t\tEND CONDITION -> NO CHOICES")