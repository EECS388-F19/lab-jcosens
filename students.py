students = ["Daniel", "Kanu", "Olivia"]
students.sort()
print(students)

first_name = students[0]
first_name = first_name[:-1]
print(first_name)
length = 0
longest = "";
for x in students:
    if len(x) > length:
        longest = x;
        length = len(x)

print(longest)
