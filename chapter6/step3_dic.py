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

Sarah_dic = dict()
Sarah_dic['Name'] = Sarah.pop(0)
Sarah_dic['DOB'] = Sarah.pop(0)
Sarah_dic['Times'] = set([sanitize(t) for t in Sarah])

print(Sarah_dic['Name']+"'s fastest are "+str(sorted(Sarah_dic['Times'])[0:3]))
