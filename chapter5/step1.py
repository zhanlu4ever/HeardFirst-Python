import sys
try:
    with open('james.txt') as James,open('julie.txt') as Julie,open('mikey.txt') as Mikey,open('sarah.txt') as Sarah:
        James_data = James.readline()
        Julie_data = Julie.readline()
        Mikey_data = Mikey.readline()
        Sarah_data = Sarah.readline()
        j = James_data.strip()
        ja = j.split(',')
        '''julie = Julie_data.strip()
        mikey = Mikey_data.strip()
        sarah = Sarah_data.strip()'''
        print(ja)

except IOError as err:
    print('err' + str(err))
