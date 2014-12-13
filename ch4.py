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