def startstopwatch(end_time,time,sleep,read,notifylim):   
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
        if now >= stop:
            string = "The Hunt will begin in "+ str(notifylim) + " minutes."
            print(string)
            for i in range(3):
                read(string)
            break


