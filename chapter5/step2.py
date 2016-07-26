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


new_James = []
new_Julie = []
new_Mikey = []
new_Sarah = []

for each_item in James_data:
    new_James.append(sanitize(each_item))
for each_item in Julie_data:
    new_Julie.append(sanitize(each_item))
for each_item in Mikey_data:
    new_Mikey.append(sanitize(each_item))
for each_item in Sarah_data:
    new_Sarah.append(sanitize(each_item))

print(sorted(new_James))
print(sorted(new_James,reverse = True))
