import requests
import sys
from time import time
from time import sleep

from Methods.timer_x import startstopwatch
from Methods.txt2speech import read

if __name__ == "__main__":
    resp = requests.get(url='https://api.warframestat.us/pc/cetusCycle', params=dict())
    data = resp.json()
    
    isDay = data["isDay"]
    timeLeft = data["timeLeft"].split()

    if isDay:
        if len(timeLeft) == 3:
            timeLeftSec = (int(timeLeft[0][:-1]) * 60 * 60) + (int(timeLeft[1][:-1]) * 60) +  int(timeLeft[2][:-1])
        elif len(timeLeft) == 2:
            timeLeftSec = (int(timeLeft[0][:-1]) * 60) +  int(timeLeft[1][:-1])
        elif len(timeLeft) == 1:
            timeLeftSec = int(timeLeft[0][:-1])
        timeLeftSecNoti = timeLeftSec
        
        notifylim = int(input("How many minutes prior do you need the notification? :"))
        # notifylim = 10
        timeLeftSecNoti -= (notifylim+1)*60
        startstopwatch(timeLeftSecNoti,time,sleep,read,notifylim, timeLeftSec)