# We wrote loops in the form below.
# The starting value for the loop variable is 0 by default.
# The values for the loop variable i go up to and not including 5.
for i in range(5):
    print(i)

print()

# Here the starting value for the loop variable
# is specified here as 1.
# The values for the loop variable i go up to and not including 5.
for i in range(1, 5):
    print(i)

print()

# Here the starting value for the loop variable
# is specified as 2.
# The values for the loop variable i go up to and not including 11,
# counting by 2s (with a "step size" of 2):
for i in range(2, 11, 2):
    print(i)

print()

print(range(5))

print()

print(type(5))
print(type(2.3))
print(type('Hello'))
print(type(False))
print(type(range(5)))
print(type([5, 3, 1, 7, 0]))

print()

print('a' + 'b')
print(str(2.3) + 'a')
print(int('5'))
print(type(range(5)))
print(list(range(5)))

print()
my_list = [5, 3, 1, 7, 0]
# Get the first three elements in the list:
print(my_list[0:3])
# We sliced the list to get the elements
# starting from index 0 and going up to and not including
# 3.
# Get the last three elements in my_list:
print(my_list[2: 5])

print()

my_string = 'giraffe'
print(my_string[0])
print(my_string[2:5])

# Make a copy of the list.
# Make a second list that's the same as the first:
copy_of_my_list = my_list[:]
print(copy_of_my_list)

# This is different than this.
copy2_of_my_list = my_list
# In general, avoid this way. It's a called a reference
# copy. It's considered dangerous.

print()

print(my_list)
# Here copy_of_my_list was created "properly".
# When I change copy_of_my_list, the change does not
# affect the original list.
copy_of_my_list[0] = -5
print(copy_of_my_list)
print(my_list)
# Here copy2_of_my_list was created with a
# reference copy, which we usually avoid, because,
# when I change copy2_of_my_list, the change
# affects the original list also.
copy2_of_my_list[-1] = 100
print(copy2_of_my_list)
print(my_list)

print()

print(my_list)

print()

for number in my_list[2:5]:
    print(number)

print()

print()

x = 1
x = 2
print(x)

# Make a copy of the list.
# Make a second list that has the same elements as the first:
copy_of_my_list = my_list[:]
print(copy_of_my_list)

print(my_list)

# Here copy_of_my_list was created "properly".
# When I change copy_of_my_list, the change does not
# affect the original list.
copy_of_my_list[0] = -5
print(f'copy_of_my_list: {copy_of_my_list}')
print(f'my_list: {my_list}')

# This is different than this.
copy_of_my_list = my_list
# In general, avoid this way. It's a called a reference
# copy. It's considered dangerous.

print()

# Here copy_of_my_list was created "improperly" as a
# reference copy.
# When I change copy_of_my_list, the change
# affects the original list.
# When I change my_list, the change affects copy_of_my_list.
copy_of_my_list[0] = 200
print(f'copy_of_my_list: {copy_of_my_list}')
print(f'my_list: {my_list}')

print()

# Create a list using list comprehension.
values = [value**2 for value in range(1, 11)]
print(values)

#print()

numbers = []
for i in range(1, 11):
    numbers.append(i**2)
print(numbers)

print()

# Lists are mutable.
print(my_list)
print(my_list[0])
my_list[0] = 500
print(my_list)

print()

# Strings are not mutable.
my_string = 'hedgehog'
print(my_string[0])
# my_string[0] = 'v' ERROR!
print(my_string)

print()

# Here is a tuple.
a_tuple = (5, 3, 1, 7, 100)
print(a_tuple)
print(a_tuple[0])

print()

for element in a_tuple:
    print(element)

# Tuples are not mutable.
# a_tuple[0] = -5 # This is doesn't work!
for element in a_tuple:
    print(element)

print()

print(my_list)
print(5 in my_list)

print()
print(f'The letter "v" is in hedgehog:'
      f' {"v" in "hedgehog"}')

print()

print("Does my my_list have any elements?")
if my_list:
    print("Yes!")
else:
    print("No!")

print()

quality_points = []
print("Does quality_points have any elements?")
if quality_points:
    print("Yes!")
else:
    print("No!")

print()

print(f'-1 is not in my_list: {-1 not in my_list}')

print()

name = input("What's your name? ")
print(f"Hello, {name}.")

# The input function interprets the user's input
# as a string!

print()

age_string = input("What's your age? ")
age = int(age_string)
if age > 60:
    print("You're old!")

print()

age = int(input("What's your age? "))
if age > 40:
    print("You're old!")




