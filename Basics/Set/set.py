
meal_set = {'breakfast', 'lunch', 'dinner', 'breakfast', 'lunch', 'dinner'}
print(meal_set)

meal_set.add('lunch snack')
meal_set.pop()  # set内の値をrandomに消去
print(meal_set)

meal_set2 = {'breakfast', 'lunch', 'dinner', 'night snack'}
print(meal_set2.difference(meal_set))  # meal_set2にあり、meal_setにないものを表示
print(meal_set.difference(meal_set2))  # meal_setにあり、meal_set2にないものを表示

# Empty set
empty_set = set()
print(type(empty_set))
empty_dict = {}  # 空のdictionaryを作成することに注意
print(type(empty_dict))
