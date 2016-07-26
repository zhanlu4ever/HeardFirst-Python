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

class Athlete:
    def __init__(self,a_name,a_dob=None,a_times=[]):
        self.name = a_name
        self.dob = a_dob
        self.times = a_times

    def top3(self):
        return(sorted(set([sanitize(t) for t in self.times]))[0:3])

    def add_time(self,time_string):
        self.times.append(time_string)

    def add_times(self,time_list):
        self.times.extend(time_list)

    def dele_time(self,time_string):
        self.times.remove(time_string)

def get_coach_data(filename):
    try:
        with open(filename) as f:
            data = f.readline()
        temp = data.strip().split(',')
        return(Athlete(temp.pop(0),temp.pop(0),temp))

    except IOError as ioerr:
        print('File error: '+str(ioerr))
        return(None)

Sarah = get_coach_data('sarah2.txt')

Sarah.add_time('1.99')
print(Sarah.name+"'s fastest are "+str(Sarah.top3())+' old')

Sarah.dele_time('1.99')
print(Sarah.name+"'s fastest are "+str(Sarah.top3())+' old')

