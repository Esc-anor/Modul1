#git config --global user.name "Esc-anor"
#git config --global user.email "romangribanov@rambler.ru"
#git bash
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
print('g-', type(grades))
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
print('s-', type(students))
grades = [(sum(grades[0]) / (len(grades[0]))), (sum(grades[1]) / (len(grades[1]))), (sum(grades[2]) / (len(grades[2]))), (sum(grades[3]) / (len(grades[3]))), (sum(grades[4]) / (len(grades[4])))]
print(grades)
a = students
grades.sort()
print(grades)
print(type(students))