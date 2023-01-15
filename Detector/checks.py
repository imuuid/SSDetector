
from os.path import isfile, getmtime
from os import listdir, system, getlogin
import time
from datetime import datetime
import psutil
import helpers as hp
from subprocess import check_output
from getpass import getuser
import Journal as j
from os.path import expandvars
from json import load
import func as f
import re

global SusFilesCheckStatus
def getAlts():
    ALLAccounts = []
    try:
            
            try:
                    f = open(expandvars(R"C:\Users\$Username\Appdata\Roaming\.minecraft\launcher_accounts.json"),'r')
                    j = load(f)
                    f.close()
                    accounts = [x['minecraftProfile']['name']for x in j["accounts"].values()]
                    ALLAccounts.append(accounts)
            except:
                    pass
            try:
                    f = open(expandvars(R"C:\Users\$Username\.lunarclient\settings\game\accounts.json"),'r')
                    j = load(f)
                    f.close()
                    vals = [x for x in j["accounts"].values()]
                    for val in vals:
                        ALLAccounts.append(val["username"])
            except:
                    pass
            try:
                    with open(expandvars(R"C:\Users\$Username\AppData\Roaming\.minecraft\usercache.json"),'r') as f:
                        AccountsList = f.read()
                        source=AccountsList
                        start_sep='{'
                        end_sep='}'
                        result=[]
                        tmp=source.split(start_sep)
                        for par in tmp:
                          if end_sep in par:
                            result.append(par.split(end_sep)[0])
                        for i in result:
                            newres = re.search('"name":"(.*)","uuid":"',i)
                            ALLAccounts.append(newres.group(1))
            except:
                    pass
    except:
            pass
    return hp.removeDuplicates(ALLAccounts)
#generic infos check



def StoppedProcessesCheck():
    StoppedProcesses = []
    services = ["DPS","PcaSvc","DiagTrack","SysMain"]
    for i in services:
        out = str(check_output(["sc", "query", i]))
        if "STOPPED" in out:
            StoppedProcesses.append(i)
            f.status = "unlegit"
    return StoppedProcesses




#Generic Scans
def recordingscan():
    results = []
    rec = {
        "obs32.exe":"OBS32",
        "obs64.exe":"OBS64",
        "bdcam.exe":"BANDICAM",
        "action_svc.exe":"ACTION",
        "XSplit.Core.exe":"XSPLIT",
        "RadeonSettings.exe":"RADEON",
        "RadeonSoftware.exe":"RADEON",
        "ShareX.exe":"SHAREX",
        "NVIDIA Share.exe":"NVIDIA",
        "CamRecorder.exe":"CAMRECORDER",
        "Fraps.exe":"FRAPS",
        "Discord.exe":"DISCORD"
        }
    
    for proc in psutil.process_iter():
        try:
            processName = proc.name()
            if processName in rec:
                results.append(processName)
                
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return hp.removeDuplicates(results)



def SusFilesCheck():
    
    SusFiles = []

    PcaRead = hp.dump(hp.getPid("PcaSvc",True))
    
    for line in PcaRead:
        line = line.strip()
        if isfile(line):
            if line.endswith(hp.getExecutableExtensions()):
                if hp.GetDigitalSignatureStatus(line) != "verified":
                    SusFiles.append(line)
        
    return hp.removeDuplicates(SusFiles)



def MovedOrRemovedFilesCheck(): # check in costruzione
    MovedOrRemovedFiles = []
    PcaSvc = open("C:\\Detector\\Processes\\PcaSvc.txt","r")
    PcaSvcRead = PcaSvc.readlines()
    PcaSvc.close()
    Explorer = open("C:\\Detector\\Processes\\explorer.txt","r")
    ExplorerRead = Explorer.readlines()
    Explorer.close()


    for ELine in ExplorerRead:
        if ELine[1:3] == ":\\" and ELine.endswith(hp.getExecutableExtensions()):
            if ELine not in PcaSvcRead:
                MovedOrRemovedFiles.append(ELine)



def BypassMethodsCheck():
    Result = ""
    Stoppeds = StoppedProcessesCheck()
    if len(Stoppeds)!=0:
        Result += "\n[!] Stopped Processes Found!"
        for i in Stoppeds:
            Result += "\n [-] " + i
        f.status = "unlegit"

    if SusFilesCheckStatus:
        SusFiles = SusFilesCheck()
        if len(SusFiles)!=0:
            Result += "\n[!] Suspicious Files Check - Not Valid/Not signed Files:"
            for i in SusFiles:
                Result += "\n - " + i
    else:
        Result += "\n[!] SUSFilesCheck unabled due to VisualStudio2015 missing dll."
    return Result

def GenericInfos():
    GenericInfosResult = ""
    mcprocess_info = {}  # thanks to https://github.com/Jammy108/AstroSS/blob/master/Astro/astro.py
    process = [p for p in psutil.process_iter(attrs=['pid', 'name']) if 'javaw' in p.info['name']]
    if process:
        process = process[0]
        pid = process.info['pid']
    try:
        process = process.cmdline()
    except:
        pass
    for argument in process:
        if "--" in argument:
            mcprocess_info[argument.split("--")[1]] = process[process.index(argument) + 1]

    modTime = getmtime("C:/$Recycle.Bin/" +
                       str(check_output(f'wmic useraccount where name="{getlogin()}" get sid')).split('\\r\\r\\n')[1])
    modTime = time.strftime('%d/%m/%Y %H:%M:%S', time.localtime(modTime))


    GenericInfosResult += "\n[+] Started / modified Times:"
    last_reboot = psutil.boot_time()  # pc started time
    GenericInfosResult += "\n  PC Start time: " + datetime.fromtimestamp(last_reboot).strftime("%d/%m/%Y %H:%M:%S")
    GenericInfosResult += "\n  explorer Start Time: " + hp.getProcessStartTime(hp.getPid("explorer.exe"))
    try:
        GenericInfosResult += "\n  DPS Start Time: " + hp.getProcessStartTime(hp.getPid("DPS", True))
    except:
        GenericInfosResult += "\n  Dps not found."
    try:
        GenericInfosResult += "\n  Javaw Start Time: " + hp.getProcessStartTime(hp.getPid("javaw.exe"))
    except:
        GenericInfosResult += "\n  Javaw not found."
    GenericInfosResult += "\n  RecycleBin Modified Time: " + modTime
    alts = getAlts()
    if len(alts) > 0:
        GenericInfosResult += "\n  Alts Found: " + str(alts)
    else:
        GenericInfosResult += "\n  No Alts Found."
    return GenericInfosResult


def GenericChecks():
    Result = ""

    RecScan = recordingscan()
    Result += "\n[+] Generic Checks:"

    if len(RecScan)!=0:
        Result += "\n[!] Recording Softwares Found!"
        for i in RecScan:
            Result += "\n - " + i

    return Result

def JournalCheck():
    res = "Journal Check " + datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    print("[*] Deleted PFS File Checking")
    with open(fr"C:\Users\{getuser()}\AppData\Local\Temp\JournalCheck.txt","w") as File:
        DeletedPFS = j.getPrefetchDeletedFiles()
        if len(DeletedPFS)!=0:
            res += "\n[!] Deleted Prefetch Files Found."
            for name,date in DeletedPFS.items():
                res += f"\n- File: {name} Elimination Date: {date}"
        DeletedFiles = j.getDeletedFiles()
        print("[*] Checking Deleted Files")
        if len(DeletedFiles)!=0:
            res += "\n[!] Deleted Files Found."
            for name, date in DeletedFiles.items():
                res += f"\n- File: {name} Elimination Date: {date}"
        print("\n[-] Check Succesfully Completed.")
        File.write(res)
        print(fr"C:\Users\{getuser()}\AppData\Local\Temp\JournalCheck.txt")
    system(fr"C:\Users\{getuser()}\AppData\Local\Temp\JournalCheck.txt")
    
            
    
