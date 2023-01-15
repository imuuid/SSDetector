import func
from getpass import getuser
from os import system
class Results:
    def __init__(self,scanID):
        self.scanID = scanID
        self.GenericInfosCheckResult = ""
        self.GenericChecksCheckResult = ""
        self.ProcessesCheckResult = ""
        self.BypassMethodsResult = ""


    def ADDGenericInfosCheck(self, s):
        self.GenericInfosCheckResult += s + "\n"
    def ADDBypassMethod(self, bypassmethod):
        self.BypassMethodsResult += bypassmethod + "\n"
    def ADDGenericCheckResult(self,r):
        self.GenericChecksCheckResult += r + "\n"
    def ADDProcessesCheckResult(self,p):
        self.ProcessesCheckResult += p + "\n"

    def PrintResults(self):
        FinalString = "Scan ID: " + self.scanID + "\nStatus: " + func.status + "\n" + self.GenericInfosCheckResult + "\n" + self.GenericChecksCheckResult + "\n" + self.ProcessesCheckResult + "\n" + self.BypassMethodsResult + "\n@SSDetectorTool"
        with open(f"C:\\Users\\{getuser()}\\Desktop\\SSDResults.txt","w") as f:
            f.write(FinalString)
