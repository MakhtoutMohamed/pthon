# print out the squares of numbers from 1 to 10 using the for loop
import os

os.system("clear")

for i in range(5):
    print(f"the square of {i} is: ", i*i)

###################################
random_things = ["Puppies", 55, "Anthony Jonh", 1/2, ["Oh", "yes", "list inside a list"]]
# here's how you access element of a list

animals = ['bear', 'tiger', 'penguin', 'zebra']
first_animal = animals[0]
print(first_animal)
third_animal = animals[2]
print(third_animal)

print("There are this many things:", len(random_things))
print("things is a:", type(random_things))

another_list = random_things[-1]
print("the last element: ", another_list)
another_list = random_things[0]
print("the first element: ", another_list)
print(type(another_list))