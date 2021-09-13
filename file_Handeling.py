filename = 'text.txt'
# ! Writing into a file
# f = open(filename, 'w')
# f.write("Hii this is a text file for testing file handeling")
# f.close()

# ? with is frequently used as there is no need to close a file if with is used
# ! Reading a File
# with open(filename) as f:
#     print(f.read())

# ! Appending into a file
with open(filename, 'a') as f:
    f.write('\nThis is appending to a file content')
