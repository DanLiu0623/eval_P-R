import os
import linecache

# f = open('demo.txt')
# f_new = open('new.txt', 'w')
#
# for index in range(len(f.readlines())):
# 	line = linecache.getline('demo.txt', index+1)
# 	if line[:5] == '/home':
# 		path = str(index) + '\n'
# 		f_new.write(path)
#
# f_org = open('demo.txt')
# f_new = open('new.txt')
# f_final = open('final.txt','w')
# for i in range(len(f_new.readlines())):
# 	i_data = linecache.getline('new.txt', i+1)
# 	start = int(linecache.getline('new.txt', i+1).strip()) + int(1)
# 	end = int(linecache.getline('new.txt', i+2).strip())
# 	# print 'lalalla', start, end
# 	for num in range(start, end): #num
# 		path = linecache.getline('demo.txt', int(i_data) + 1).strip()
# 		file = path + ',' + linecache.getline('demo.txt', int(num) + 1).strip()  +'\n'
# 		f_final.write(file)



#
f = open('final.txt')
result = open('result5.txt', 'w')
for line in f.readlines():
	new = line.replace('JPEGImages', 'labels').replace('jpg', 'txt').replace('wrc','ld')
	# new = line.replace('wrc', 'ld')
	print new
	result.write(new)









# for eachline in f.readlines():
# 	print eachline
# 	if eachline[:5] == '/home':
# 		path = eachline
# 		print path




