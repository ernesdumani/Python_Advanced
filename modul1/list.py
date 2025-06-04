name_of_the_list=['item1', 'item2', 'item3']

to_do_list=['math_homework', 'research for biology', 'clean_the_room', 'fun']

first_item=to_do_list[0]
second_item=to_do_list[1]
third_item=to_do_list[2]
forth_item=to_do_list[3]

print(first_item)
print(second_item)

favorite_colors=['red', 'yellow', 'orange', 'green', 'blue']
print(favorite_colors[0])

shopping_list=['apple', 'oranges', 3, 3.5,]
#shopping_list.append('milk')
shopping_list.insert(2, 'milk')

print(shopping_list)
to_do_list.remove('math_homework')
print(to_do_list)

del shopping_list[1]
print(shopping_list)

to_do_list[1]="research for math"
print(to_do_list)

print("hello world!")