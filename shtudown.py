import os 
shutdown = input("Shutdown your pc ? (yes/no)")
if shutdown.lower =="no":
    exit
else:
     os.system("shutdown /s /t 0")