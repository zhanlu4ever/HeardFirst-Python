man = []
other = []

try:
	data = open('F:\HeadFirstPython\Chapter3\chapter3\sketch.txt')
	for each_line in data:
		try:
			(role,line_spoken) = each_line.split(':',1)
			line_spoken = line_spoken.strip()
			if role == 'Man':
				man.append(line_spoken)
			elif role == 'Other Man':
				other.append(line_spoken)
		except ValueError:
			pass
except IOError:
	print('The datafile is missing')


try:
        with open('man_data.txt','w') as man_data,open('other_data.txt','w') as other_data:
                print(man,file=man_data)
                print(other,file = other_data)          
except IOError as err:
	print("please set file" + str(err))

	
