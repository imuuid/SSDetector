
from ntpath import join
import checks as chs
from threading import Thread
from os import system
import helpers as hp
import ProcessesCheck as pc
from datetime import datetime

def dump_processes():
    try:
        hp.dump(hp.getPid('explorer.exe'),"C:\\Detector\\Processes\\explorer.txt")
        #hp.dump(hp.getPid('DPS',True),"C:\\Detector\\Processes\\dps.txt")
        hp.dump(hp.getPid('PcaSvc',True),"C:\\Detector\\Processes\\PcaSvc.txt")
    except Exception as e:
        print("errore nel dump. Error type: " + e)

def CheckHeader():
    print("do u want journal? y/n")
    r = input()
    system("cls")
    start_time = datetime.now()
    dump_processes()
    Thread(target = chs.GenericInfos).start()
    Thread(target = chs.GenericChecks).start()
    Thread(target = pc.ProcessesChecks()).start()
    chs.BypassMethodsCheck()

    if r == "y":
        Thread(target = chs.JournalCheck()).start()
    #print(f"\nCheck executed Time: {(datetime.now()-start_time).total_seconds()*1000} ms")
    print("\n\nAll checks are done. nesty#5542,@ulteriordll")
    print("Press a key.")
    input()
    hp.destruct()
    

    
    









