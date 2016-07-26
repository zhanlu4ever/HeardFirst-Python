import os
os.chdir('F:\HeadFirstPython\Mine\chapter5')
def sanitize(time_string):
    if '-' in time_string:
        spliter = '-'
    elif ':' in time_string:
        spliter = ':'
    else:
        return time_string

    (mins,secs) = time_string.split(spliter)
    return(mins+'.'+secs)


with open('james.txt') as James:
    data = James.readline()
James_data = data.strip().split(',')

with open('julie.txt') as Julie:
    data = Julie.readline()
Julie_data = data.strip().split(',')

with open('mikey.txt') as Mikey:
    data = Mikey.readline()
Mikey_data = data.strip().split(',')

with open('sarah.txt') as Sarah:
    data = Sarah.readline()
Sarah_data = data.strip().split(',')

'''
new_James = [sanitize(each_item) for each_item in James_data]
new_Julie = [sanitize(each_item) for each_item in Julie_data]
new_Mikey = [sanitize(each_item) for each_item in Mikey_data]
new_Sarah = [sanitize(each_item) for each_item in Sarah_data]
'''

print(sorted([sanitize(each_item) for each_item in James_data]))
#print(sorted(new_James,reverse = True))
print(James_data[0:3])   #show j_d[0][1][2] three data

james = sorted([sanitize(each_item) for each_item in James_data])

unique_james = []

for each_item in james:
    if each_item not in unique_james:
        unique_james.append(each_item)
        
#print(unique_james[0:3])
print(sorted(set(james))[0:4]) 
