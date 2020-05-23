employee_file = open("employees.txt", "r")  # (r)ead (w)rite (a)ppend r+

print(employee_file.readable())  # readable depends on open mode (r)
# print(employee_file.readline())  # first line
# print(employee_file.readline())  # second line

for employee in employee_file.readlines():
    print(employee)

employee_file.close()  # always close a file similar to closing a stream c#

employee_file = open("employees.txt", "a")  # (r)ead (w)rite (a)ppend r+
#  Be careful when appending to files
employee_file.write("\nToby, Human Resources")

employee_file.close()  # always close a file similar to closing a stream c#

employee_file = open("employees1.txt", "w")  # (r)ead (w)rite (a)ppend r+
#  Writing to a file means to overwrite
employee_file.write("\nToby, Human Resources")

employee_file.close()  # always close a file similar to closing a stream c#

html_file = open("index.html", "a")  # (r)ead (w)rite (a)ppend r+
#  Writing to a file means to overwrite
html_file.write("<p>This is some HTML<p>")

html_file.close()  # always close a file similar to closing a stream c#

