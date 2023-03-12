def startstopwatch(end_time,time,sleep,read,notifylim, timeleft):   
    now = int(time())
    stop = now + end_time
    if stop < now:
        string = "Your desired time has already passed."
        read(string)
        return
    print("Timer running ...")
    while True:
        sleep(1)
        now += 1
        if (stop-now)%60 == 0:
            string = f"The Hunt will begin in about {timeleft//60} minutes."
            print(string)
        if now >= stop:
            string = f"The Hunt begins in about {str(notifylim)} Minutes Tenno. Prepare for the hunt."
            print(string)
            read(string)
            break


