import os
os.chdir('F:\HeadFirstPython\Mine\chapter6')
def sanitize(time_string):
    if '-' in time_string:
        spliter = '-'
    elif ':' in time_string:
        spliter = ':'
    else:
        return time_string

    (mins,secs) = time_string.split(spliter)
    return(mins+'.'+secs)

def get_coach_data(filename):
    try:
        with open(filename) as f:
            data = f.readline()
        return(data.strip().split(','))
    except IOError as ioerr:
        print('File error: '+str(ioerr))
        return(None)

Sarah = get_coach_data('sarah2.txt')
(Sarah_name,Sarah_dob) = Sarah.pop(0),Sarah.pop(0)
print(Sarah_name+"'s fastest time are: "+str(sorted(set([sanitize(t) for t in Sarah]))[0:3]))
