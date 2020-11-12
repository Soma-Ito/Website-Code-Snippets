
# Excercise 1 Answer
lst = []
for num in range(101):
    lst.append(num)

# Excercise 1 Another Answer
lst = [num for num in range(101)]

# Excercise 2 Answer
new_lst = []
for item in lst:
    if item % 2 == 0:
        new_lst.append(2 * item)
    else:
        new_lst.append(2 * (item + 1))

# Excercise 3 Answer
print(new_lst)
