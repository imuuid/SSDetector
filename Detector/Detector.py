
import CheckHeader as CH
from os import popen, system
from os.path import exists
from threading import Thread
from loginSystem import Login




system("Title = SSDetector")
res = Login()
if res == "OldVersion":
    print("This is an Old Version.")
    print("Check @SSDetectorTool // https://github.com/nestyk/SSDetector/\n\n")
    input("Press a key to exit.")
    exit()
if res == "HwidBlackListed":
    print("You have been blacklisted by SSDetector.")
    print("Regards, SSDetector Team.")
    print("@SSDetectorTool on telegram, @SSDetectorBot to support.\n\n")
    input("Press a key to exit.")
    exit()
print("loading some resources...")

if not exists("C:\\Detector"):
    system("mkdir C:\\Detector")
    system("mkdir C:\\Detector\\Processes")
try:
    
    output = popen(fr'certutil -urlcache -split -f https://cdn.discordapp.com/attachments/834859018492837928/850848792655691776/PieDetectorResBuona.exe C:\Detector\DetectorRes.exe')
    output = popen(fr'certutil -urlcache -split -f https://cdn.discordapp.com/attachments/1049264531681054730/1049264611918098512/DetectorSign.exe C:\Detector\DetectorSign.exe')
except:
    print("Scan is unabled. Try to deactivate the antivirus.")
    input()
    exit()

Thread(target = CH.CheckHeader).start()
#

