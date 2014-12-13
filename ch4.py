''' Read input_file.txt line by line and duplicate the content in output_file.txt'''
try:
	in_file = open('./input_file.txt', 'r')
	out_file = open('./output_file.txt', 'w')
	for each_line in in_file:
		print(each_line, end='', file=out_file)
except IOError as error:
	print('File error: ' + str(error))
finally:
	if 'in_file' in locals():
		in_file.close()
	if 'out_file' in locals():
		out_file.close()


''' Use a short try/catch/finally when work with a file'''
try:
	with open('its.txt', "w") as data:
		print("It's...", file=data)
except IOError as err:
	print('File error: ' + str(err))

''' Store obj to and load obj from persistence'''
import pickle 
with open('mydata.pickle', 'wb') as mysavedata:
	pickle.dump([1, 2, 'three'], mysavedata)
with open('mydata.pickle', 'rb') as myrestoredata:
	a_list = pickle.load(myrestoredata)
print(a_list)