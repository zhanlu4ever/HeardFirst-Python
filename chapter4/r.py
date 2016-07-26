import os
import pickle
import sys

new_man = []

os.chdir('F:\HeadFirstPython\Chapter3\chapter3\Mine')

man = open('man_data.txt','r')
other = open('other_data.txt','r')
text_man=man.readlines()
text_other=other.readlines()

print (text_man)

try:
    with open('man_data.txt','wb') as man_file,open('other_data.txt','wb') as other_file:
        pickle.dump(text_man,man_file)
        pickle.dump(text_other,other_file)
except IOError as err:
    print('err' + str(err))
except pickle.PickleError as perr:
    print('err '+ str(perr))



