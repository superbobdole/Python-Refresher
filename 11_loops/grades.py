grades = [35, 67, 98, 100, 100]
total = 0
amount = len(grades)

#for statement creates a new variable 'grade'
for grade in grades:
    total += grade

print(total / amount)

#you can also just use total = sum(grades) divided by len(grades)