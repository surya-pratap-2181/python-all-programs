# You are given a string S.
# Your task is to find out if the string S contains: alphanumeric characters, alphabetical characters, digits, lowercase and uppercase characters.
s = input()
# Solution 1
# print(any(map(str.isalnum,s)))
# print(any(map(str.isalpha,s)))
# print(any(map(str.isdigit,s)))
# print(any(map(str.islower,s)))
# print(any(map(str.isupper,s)))
# Solution 2
print(any(c.isalnum() for c in s))
print(any(c.isalpha() for c in s))
print(any(c.isdigit() for c in s))
print(any(c.islower() for c in s))
print(any(c.isupper() for c in s))
