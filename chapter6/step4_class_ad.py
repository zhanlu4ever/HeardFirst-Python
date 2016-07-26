import os
os.chdir('F:\HeadFirstPython\Mine\chapter6')

from step4_class import Athlete
#有四个输出，两个是输入类的

def sanitize(time_string):
    if '-' in time_string:
        spliter = '-'
    elif ':' in time_string:
        spliter = ':'
    else:
        return time_string

    (mins,secs) = time_string.split(spliter)
    return(mins+'.'+secs)

class Athletelist(list):
    def __init__(self,a_name,a_dob=None,a_times=[]):
        list.__init__([])
        self.name = a_name
        self.dob = a_dob
        self.extend(a_times)

    def top3(self):
        return(sorted(set([sanitize(t) for t in self]))[0:3])

def get_coach_data(filename):
    try:
        with open(filename) as f:
            data = f.readline()
        temp = data.strip().split(',')
        return(Athletelist(temp.pop(0),temp.pop(0),temp))

    except IOError as ioerr:
        print('File error: '+str(ioerr))
        return(None)

Sarah = get_coach_data('sarah2.txt')


Sarah.append('1.99')
print(Sarah.name+"'s fastest are "+str(Sarah.top3()))

Sarah.remove('1.99')
print(Sarah.name+"'s fastest are "+str(Sarah.top3()))
