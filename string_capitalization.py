# string = 'hello World'
# s = string.split()
# s = [word.capitalize() for word in s]
# s = " ".join(s)
# print(s)

s = input()
for x in s[:].split():
    s = s.replace(x, x.capitalize())
print(s)
