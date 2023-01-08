
import checks as chs
from threading import Thread
from os import system
import helpers as hp
import ProcessesCheck as pc
from os.path import exists
from func import SendResult
from random import choice
def dump_processes():
    try:
        hp.dump(hp.getPid('explorer.exe'),"C:\\Detector\\Processes\\explorer.txt")
        #hp.dump(hp.getPid('DPS',True),"C:\\Detector\\Processes\\dps.txt")
        hp.dump(hp.getPid('PcaSvc',True),"C:\\Detector\\Processes\\PcaSvc.txt")
    except Exception as e:
        print("errore nel dump. Error type: " + e)

def CheckHeader():
    scanID = "".join(choice('ABCDEFGHJKLMNPQRSTUVWXYZ123456789') for i in range(1, 7))
    if not exists("C:\\Windows\\System32\\VCRUNTIME140D.dll"):
        chs.SusFilesCheckStatus = False
    else:
        chs.SusFilesCheckStatus = True
    print("do u want journal? y/n")
    r = input()
    system("cls")
    dump_processes()
    Thread(target = chs.GenericInfos).start()
    Thread(target = chs.GenericChecks).start()
    Thread(target = pc.ProcessesChecks()).start()
    Thread(target = chs.BypassMethodsCheck()).start()
    SendResult(scanID)
    if r.lower() == "y":
        chs.JournalCheck()
    print("\n\nAll checks are done. nesty#5542,@ulteriordll")
    print("Press a key.")
    input()
    hp.destruct()
    

    
    









