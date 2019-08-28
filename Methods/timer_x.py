def startstopwatch(end_time,time,sleep,read,notifylim):   
    now = int(time())
    stop = now + end_time
    
    while True:
        sleep(1)
        now += 1
        if now >= stop:
            string = "The Hunt will begin in "+ str(notifylim-1) + " minutes."
            print(string)
            for i in range(3):
                read(string)
            break


