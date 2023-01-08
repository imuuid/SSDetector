from os import system
from helpers import getJavawStartTime
#Journal Strings
#deleted files: fsutil usn readjournal c: csv | findstr /i /C:"%date%" | findstr /i /C:"0x80000200" | findstr /i /C:.exe\^" /i /C:.pf\^" /i /C:.com\^ /i /C:.jar\^" /i /C:.pif\^" /i /C:.mp4\^" /i /C:.bat\^ /i /C:.sys\^" /i /C:.zip\^" /i /C:.cmd\^" /i /C:.?\^" /i /C:.vb\^" /i /C:.shs\^" /i /C:.com\^ /i /C:.rar\^" /i /C:.docx\^" /i /C:.doc\^" /i /C:.reg\^" > DeletedFiles.txt
#rename: fsutil usn readjournal c: csv | findstr /i /C:"%date%" | findstr /i /C:"0x00102000" /i /C:"0x00101000" /i /C:"0x00001000" /i /C:"0x00002000" | findstr /i /C:.exe\^" /i /C:.pf\^" /i /C:.com\^ /i /C:.jar\^" /i /C:.pif\^" /i /C:.mp4\^" /i /C:.bat\^ /i /C:.sys\^" /i /C:.zip\^" /i /C:.cmd\^" /i /C:.?\^" /i /C:.vb\^" /i /C:.shs\^" /i /C:.com\^ /i /C:.rar\^" /i /C:.docx\^" /i /C:.doc\^" /i /C:.reg\^" > renamed.txt
#cacls: fsutil usn readjournal c: csv | findstr /i /C:"%date%" | findstr /i /C:"0x00000800"| findstr /i /C:"0x00000c30" /i /C:"0x00000010" | findstr /i /C:"Prefetch" > modificadisicurezza.txt
#jnativehook: fsutil usn readjournal c: csv | findstr /i /C:"%date%" | findstr /i /C:"JnativeHook" | findstr /i /C:".dll" > Jar.txt

def getPrefetchDeletedFiles():
    PFDeleted = {}
    system('fsutil usn readjournal c: csv | findstr /i /C:"0x80000200" | findstr /i /C:".pf" | findstr /i /C:"%date%" > C:\\Detector\\DeletedPrefetchFiles.txt')
    with open("C:\\Detector\\DeletedPrefetchFiles.txt") as DPF:
      
        for line in DPF.read().splitlines():
            if line.split(",")[5][1:-1] > getJavawStartTime():
                PFDeleted[line.split(",")[1][1:-1]] = line.split(",")[5][1:-1]
    system("del C:\\Detector\\DeletedPrefetchFiles.txt")
    return PFDeleted
        
def getDeletedFiles():
    DeletedFiles = {}
    system('fsutil usn readjournal c: csv | findstr /i /C:"%date%" | findstr /i /C:"0x80000200" | findstr /i /C:.exe\^" /i /C:.py\^" /i /C:.com\^ /i /C:.jar\^" /i /C:.pif\^" /i /C:.mp4\^" /i /C:.bat\^ /i /C:.sys\^" /i /C:.zip\^" /i /C:.cmd\^" /i /C:.?\^" /i /C:.vb\^" /i /C:.shs\^" /i /C:.com\^ /i /C:.rar\^" /i /C:.docx\^" /i /C:.doc\^" /i /C:.reg\^" > C:\\Detector\\DeletedFiles.txt')
    with open("C:\\Detector\\DeletedFiles.txt") as DF:
        for line in DF.read().splitlines():
            if line.split(",")[5][1:-1] > getJavawStartTime():
                DeletedFiles[line.split(",")[1][1:-1]] = line.split(",")[5][1:-1]
    system("del C:\\Detector\\DeletedFiles.txt")
    return DeletedFiles