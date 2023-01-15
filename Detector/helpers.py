from os import popen, system
from os.path import getmtime
from datetime import datetime
from psutil import Process, process_iter
from time import strftime, localtime
from subprocess import check_output

def getPid(name, service=False):
        if service:
            response = str(check_output(f'tasklist /svc /FI "Services eq {name}')).split('\\r\\n')
            for process in response:
                if name in process:
                    pid = process.split()[1]
                    return pid
        else:
            try:
                pid = [p.pid for p in process_iter(attrs=['pid', 'name']) if name == p.name()][0]
                return pid
            except:
                return 0
            
def getProcessStartTime(pid):
    process = Process(int(pid))
    process.create_time()
    return strftime("%d/%m/%Y %H:%M:%S", localtime(process.create_time()))

def getJavawStartTime():
    return getProcessStartTime(getPid("javaw.exe"))


def modification_date_day(filename):
    t = getmtime(filename)
    return datetime.fromtimestamp(t).strftime('%Y-%m-%d')

def usn_get_name_by_id(id):
    output = popen(fr"fsutil file queryfilenamebyid C:\ {id}").read()
    output = output.replace("Nome collegamento causale al file: \\\\?\\" ,"")
    return output

def dump(pid): #thx astross
    cmd = f'C:/Detector/DetectorRes.exe -pid {pid} -raw'
    strings = str(check_output(cmd)).replace("\\\\","/")
    strings = list(set(strings.split("\\r\\n")))
    return strings

def destruct():
    system("del C:\\Detector\\DetectorRes.exe")
    system("del C:\\Detector\\DetectorSign.exe")
    #system("del C:\\Detector\\Processes\\dps.txt")
    #system("del C:\\Detector\\Processes\\explorer.txt")
    #system("del C:\\Detector\\Processes\\PcaSvc.txt")

def getExecutableExtensions():
    return (".exe",".com",".pif",".bat",".cmd",".run",".jar",".py")

def GetDigitalSignatureStatus(dir):
    return check_output(['C:\\Detector\\DetectorSign.exe', dir]).decode('utf-8')

def removeDuplicates(x):
    return list(dict.fromkeys(x))
        
        
        






