from os import strerror

try:
    s = open("E:/pythonProject5/vvv.txt", "rt", encoding = "UTF-8")
    for i in range(10):
        line = file1.readline()
        
    s.close()
except IOError as err:
    print("I/O error occured:", strerror(err.errno))

# Python program to
# demonstrate readline()

L = ["Geeks\n", "for\n", "Geeks\n"]

# Writing to a file
file1 = open('myfile.txt', 'w')
file1.writelines((L))
file1.close()

# Using readline()
file1 = open('myfile.txt', 'r')
count = 0

while True:
	count += 1

	# Get next line from file
	line = file1.readline()

	# if line is empty
	# end of file is reached
	if not line:
		break
	print("Line{}: {}".format(count, line.strip()))

file1.close()


# from os import strerror
#
# try:
#     count = 0
#     s = open("E:/pythonProject5/vvv.txt", "rt", encoding = "UTF-8")
#     char = s.readline(1)
#
#     while char != "":
#         print(char, end = "")
#         count += 1
#         char = s.read(1)
#     s.close()
#     print("\n\n Символов в файле", count)
# except IOError as err:
#     print("I/O error occured:", strerror(err.errno))

# with open("E:/pythonProject5/vvv.txt, "r") as file1:
#     # итерация по строкам
#     for line in file1:
#         print(line.strip())
