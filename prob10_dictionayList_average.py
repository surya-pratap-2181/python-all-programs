'''
The provided code stub will read in a dictionary containing key/value pairs of name:[marks] for a list of students. Print the average of the marks array for the student name provided, showing 2 places after the decimal.
marks key:value pairs are
'alpha':[20,30,40]
'beta':[50,40,70]
query_name = 'beta'

The query_name is 'beta' average score is (50+40+70)/3=53.33

Input format:
The first line contains the integer n, the number of students' records. The next n lines contain the names and marks obtained by a student, each value separated by a space. The final line contains query_name, the name of a student to query.

Output format:
Print one line: The average of the marks obtained by the particular student correct to 2 decimal places.
'''
n = int(input())
student_marks = {}
for _ in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores
query_name = input()
student = student_marks[query_name]
total = 0
for i in student:
    total += i
average = total/len(student)
print("{:.2f}".format(average))
