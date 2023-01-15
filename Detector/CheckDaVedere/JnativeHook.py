def JnativeHookTempCheck():
    today = datetime.today().strftime('%Y-%m-%d')
    TempFolder = f"C:\\Users\\{getuser()}\\AppData\\Local\\Temp\\"
    for file in listdir(TempFolder):
        if "jnativehook" in file.lower():
            MTimeFile = hp.modification_date_day(TempFolder+file)
            return MTimeFile==today
        else:
            return False

    if JnativeHookTempCheck():
        Result += "\n[!] JnativeHook found in temp folder. Jar Autoclicker started today."
        f.status = "unlegit"