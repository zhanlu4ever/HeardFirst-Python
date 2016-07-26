import os
import pickle
import sys

new_man = []
new_other = []
os.chdir('F:\HeadFirstPython\Chapter3\chapter3\Mine')

man_temp = open('man_data.txt')
other_temp = open('other_data.txt')

man = man_temp.readlines()
other = other_temp.readlines()

try:
    with open('man_file.txt','wb') as man_file,open('other_file.txt','wb') as other_file:
        pickle.dump(man,man_file)
        pickle.dump(other,other_file)
except IOError as err:
    print('err' + str(err))
except pickle.PickleError as perr:
    print('err '+ str(perr))

try:
    with open('man_file.txt','rb') as man_f,open('other_file.txt','rb') as other_f:
        new_man = pickle.load(man_f)
        new_other = pickle.load(other_f)
except IOError as err:
    print('err '+str(err))

print(new_man)
