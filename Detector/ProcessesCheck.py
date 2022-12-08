import helpers as hp
import urllib.request

                    



def ExplorerCheck():
    f = open("C:\\Detector\\Processes\\explorer.txt")
    ExplorerLines = f.read().splitlines()
    f.close()
    PcaClient = []
    FileUsed = [] 

    for line in ExplorerLines:
        if "TRACE,0000,"in line and ",PcaClient,MonitorProcess," in line:
            PcaClient.append(line.split(",")[5])
        if line.startswith("file:///"):
            for ex in hp.getExecutableExtensions():
                if line.endswith(ex):
                    FileUsed.append(line)
    FileUsed = hp.removeDuplicates(FileUsed)
    return PcaClient, FileUsed
        



def ProcessesChecks():
    PcaClient, FileUsed = ExplorerCheck()
    if len(PcaClient) == 0:
        print("[!] Warning: PcaClient is empty. (Possible Explorer Restart).")
    elif len(PcaClient) <=7:
        print("\n\n")
        print("[!] Warning: PcaClient does not reach 8 items.")
        for p in PcaClient:
            print(" - " + p)
    if len(FileUsed)>0:
        print("\n\n[-] Started/Used Files:")
        for f in FileUsed:
            print(" - " + f)
        print("\n\n")





