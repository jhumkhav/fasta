def line_count(file_name):
    count = 0
    file = open(file_name)
    for line in file:
        line = line.strip()
        count += 1
    return count

def head_count(file_name):
    count = 0
    file = open(file_name)
    for line in file:
        if line[0] == ">":
            count += 1
    return count
        

file_name = input("Enter file name: ")
lines = line_count(file_name)
headers = head_count(file_name)
print (lines, headers)
