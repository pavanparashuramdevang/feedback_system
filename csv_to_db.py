import csv
from student_model import Student_table



filename="student_details_csv.csv"

fields=[]
rows=[]

with open(filename,'r') as csvfile:
    csvreader=csv.reader(csvfile)
    fields=next(csvreader)

    for row in csvreader:
        rows.append(row)

student=Student_table()

try:
    for row in rows:
        student.add_student(row[0],row[1])

except:
    print("some error")
