grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
avg_grades = []
avg_names = {}

for i in grades:
    avg_mark = [sum(i)/len(i)]
    avg_grades.extend(avg_mark)

stud_list = sorted(students)


for i in range(0, len(stud_list)):
    avg_names[stud_list[i]] = avg_grades[i]


print(avg_grades)
print(stud_list)
print(avg_names)


