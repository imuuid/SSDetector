
import checks as chs
from threading import Thread
from os import system
import helpers as hp
import ProcessesCheck as pc
from os.path import exists
from func import SendResult
from random import choice
from SSDResults import Results
from getpass import getuser

def CheckHeader():
    scanID = "".join(choice('ABCDEFGHJKLMNPQRSTUVWXYZ123456789') for i in range(1, 7))
    chs.SusFilesCheckStatus = False
    if not exists("C:\\Windows\\System32\\VCRUNTIME140D.dll"):
        chs.SusFilesCheckStatus = False
    else:
        chs.SusFilesCheckStatus = True
    print("do u want journal? y/n")
    r = input()
    system("cls")
    ResultsMain = Results(scanID)
    print("[*] Checking Generic Infos")
    GenericInfosResult = chs.GenericInfos()
    ResultsMain.ADDGenericInfosCheck(GenericInfosResult)
    print("[*] Checking Generic Checks")
    GenericChecksResult = chs.GenericChecks()
    ResultsMain.ADDGenericCheckResult(GenericChecksResult)
    print("[*] Checking Processes Checks")
    ProcessesCheckResult = pc.ProcessesChecks()
    ResultsMain.ADDProcessesCheckResult(ProcessesCheckResult)
    print("[*] Checking Bypass Methods")
    BypassMethodsResult = chs.BypassMethodsCheck()
    ResultsMain.ADDBypassMethod(BypassMethodsResult)
    ResultsMain.PrintResults()
    SendResult(scanID)
    system(f"C:\\Users\\{getuser()}\\Desktop\\SSDResults.txt")
    if r.lower() == "y":
        chs.JournalCheck()
    print("\n\nAll checks are done. nesty#5542,@ulteriordll")
    print("Press a key.")
    input()
    hp.destruct()
    

    
    









