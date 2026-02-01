class sentohere:

    Avalues = 0
    Bvalues = 0

    def __init__(self,value,choicetomake):
        self.iliketo = ""
        if choicetomake == 1:
            sentohere.Avalues = value
        if choicetomake == 2:
            sentohere.Bvalues = value

    def getinstance(self, objin):
        self.iliketo = objin

    def moveit(self):
        print(f"itworked {sentohere.Avalues}")
        print(f"itworked {sentohere.Bvalues}")

    def runfromout(self):
        self.iliketo.moveit()

    def randomprint(self):
        print("this is so radom")

    sentohere.randomprint()