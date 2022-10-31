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
print(my_list[2 : 5])

print()

my_string = 'giraffe'
print(my_string[0])
print(my_string[2:5])

# Make a copy of the list.
# Make a second list that's the same as the first:
copy_of_my_list = my_list[:]
print(copy_of_my_list)

#This is different than this.
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







