import subprocess
from time import *
import datetime
import ctypes

def runwithsleep(a,delay=True) :
    si = subprocess.STARTUPINFO()
    si.dwFlags |= subprocess.STARTF_USESHOWWINDOW
    subprocess.call('cmd /c '+a, startupinfo=si)
    if delay : sleep(40)

while 1 :
    day=datetime.datetime.now().strftime('%D')
    try :
        with open('day','r') as f : oldday=f.read()
    except : oldday=''

    if day!=oldday and datetime.datetime.now().hour>9 :
        with open('day','w') as f : f.write(day)

        runwithsleep('taskkill -im HD-Player.exe /f')
        runwithsleep(r'start "" "C:\Program Files\BlueStacks_nxt\HD-Player.exe" --instance Nougat64_41')

        #update apk
        runwithsleep('adb connect 127.0.0.1:5965')
        runwithsleep('adb -s 127.0.0.1:5965 shell am start -a android.intent.action.VIEW -d market://details?id=com.bandainamcogames.dbzdokkanww')
        runwithsleep('adb -s 127.0.0.1:5965 shell input tap 379 379')

        runwithsleep('adb -s 127.0.0.1:5965 shell monkey -p com.bandainamcogames.dbzdokkanww -c android.intent.category.LAUNCHER 1')
        runwithsleep('adb -s 127.0.0.1:5965 shell input tap 387 680')
        runwithsleep('adb -s 127.0.0.1:5965 shell input tap 387 680')
        runwithsleep('adb -s 127.0.0.1:5965 shell input tap 387 680')
        runwithsleep('adb -s 127.0.0.1:5965 shell input tap 387 680') #download button
        runwithsleep('adb -s 127.0.0.1:5965 shell input tap 269 576') #download completed button
        runwithsleep('adb -s 127.0.0.1:5965 shell input tap 269 576')
        runwithsleep('adb -s 127.0.0.1:5965 shell input tap 269 576')
        runwithsleep('adb -s 127.0.0.1:5965 shell input tap 300 880') #gift button

        runwithsleep('taskkill -im HD-Player.exe /f')


    sleep(3600)
