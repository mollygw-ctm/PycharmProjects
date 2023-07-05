# 1. 15 neds to be written as an integer rather than a string

# 2.
my_name = "Penelope"
my_age = 29
message = 'My name is {} and I am {} years old'.format(my_name, my_age)
print(message)

# 3.
# number of eggs per box
box_eggs = 6
# number of eggs required to make omelette
omelette = 4
# number of boxes
boxes_eggs = 6
# number of eggs across multiple boxes
eggs = (box_eggs * boxes_eggs)
# number of omelettes made
made_omelettes = eggs / omelette
output = 'You can make {} with {} boxes of eggs'.format(made_omelettes, boxes_eggs)
print(output)