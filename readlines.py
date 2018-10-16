def lines (file_name):
	fasta = open(file_name)
	count = 0
	for line in fasta:
		count += 1
	return count

def headers (file_name):
	fasta = open(file_name)
	count = 0
	for line in fasta:
		if line[0] == ">":
			count += 1
	return count

file_name = input("Enter file name: ")
lines = lines(file_name)
header = headers(file_name)
print ("Lines: ", lines, "\nHeaders: ", header)
