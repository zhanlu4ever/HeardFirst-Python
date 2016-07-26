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
        '''
        data = data.strip().split(',')
        dic = {}
        dic['Name'] = data.pop(0)
        dic['DOB'] = data.pop(0)
        dic['Times'] = set([sanitize(t) for t in data])
        return(dic)
        '''
        temp = data.strip().split(',')
        return({'Name':temp.pop(0),
                'DOB':temp.pop(0),
                'Times':str(sorted(set([sanitize(t) for t in temp]))[0:3])})

    except IOError as ioerr:
        print('File error: '+str(ioerr))
        return(None)

Sarah = get_coach_data('james2.txt')

#print(Sarah['Name']+"'s fastest are "+str(sorted(Sarah['Times'])[0:3]))
print(Sarah['Name']+"'s fastest are "+Sarah['Times'])
