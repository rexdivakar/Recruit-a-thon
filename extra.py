import time

def time_stamp():               # fetches time stamp for the log Input
    secondsSinceEpoch = time.time()
    timeObj = time.localtime(secondsSinceEpoch)

    return ('%d/%d/%d %d:%d:%d' % (
        timeObj.tm_mday, timeObj.tm_mon, timeObj.tm_year, timeObj.tm_hour, timeObj.tm_min, timeObj.tm_sec))


def write_log(log_data):        # writes log
    f = open(r'Extras\logfile.txt', 'a+')
    f.write(log_data+' '+str(time_stamp())+'\n')
    return


def get_password():             #Loads the password
    try:
        with open(r'Extras\pas.1', 'r') as f:
            password = f.read()
        write_log('Password load successfull')
        return password
    except:
        write_log('Password load failed')
        exit()
