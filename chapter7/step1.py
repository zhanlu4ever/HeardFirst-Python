import os
import pickle
os.chdir('F:\HeadFirstPython\Mine\chapter7')

from athletelist import Athletelist

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
        temp = data.strip().split(',')
        return(Athletelist(temp.pop(0),temp.pop(0),temp))

    except IOError as ioerr:
        print('File error: '+str(ioerr))
        return(None)

def put_to_store(files_list):
    all_athletes = {}

    for each_file in files_list:
        data = get_coach_data(each_file)
        #all_athletes = data
        all_athletes[data.name] = data

    try:
        with open('Athlete.pickle','wb') as ath:
            pickle.dump(all_athletes,ath)
    except pickle.PickleError as perr:
        print('error '+str(perr))
        
    return(all_athletes)

def get_from_store():
    all_athletes = {}
    try:
        with open('Athlete.pickle','rb') as ath:
            #data = pickle.load(ath)
            all_athletes = pickle.load(ath)
    except pickle.PickleError as perr:
        print('error '+str(perr))

    #all_athletes = data
    return(all_athletes)

name = ['james2.txt','sarah2.txt']
put_to_store(name)
c = get_from_store()

print(c)
