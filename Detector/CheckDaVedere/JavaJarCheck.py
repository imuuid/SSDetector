def JavaJar(): # checks.py
    results = ""
    IsThereJavaString = False
    CheatName = ""
    f = open("C:\\Detector\\Processes\\explorer.txt")
    Lines = f.read().split("\n")
    f.close()
    for line in Lines:
        if "-jar" in line and line.endswith(".jar"):
            IsThereJavaString = True
            CheatName = line.split(" ")[-1]
    for file in listdir("C:\\Windows\\Prefetch"):
        if "JAVA.EXE" in file:
            if len(CheatName) == 0:
                break
            if hp.modification_date_day("C:\\Windows\\Prefetch\\" + file) == datetime.today().strftime(
                    '%Y-%m-%d') and IsThereJavaString:
                if len(results) != 0:
                    results += "," + CheatName
                else:
                    results += CheatName

    return results


    #JavaJarFile = JavaJar()
    #if len(JavaJarFile)!=0:
        #print("[!] Java Jar Bypass Method Found!")
        #print(" - " +JavaJarFile)
        #f.status = "unlegit"
        #for i in JavaJarFile:
            #print(" [-] " + i) bypassmethods
