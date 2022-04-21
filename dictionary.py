# states = ['NW', 'PA', 'CA']
# states = ['New York', 'Pennsylvania', 'California']
# states = ['New York', 'NY', 'Pennsylvania', 'PA','California', 'CA']

import os

os.system("clear")

states = {'NY': 'New York', 'PA': 'Pennsylvania', 'CA': 'California'}

print(states['NY'])

people = ["MA", "FA"]
# print(people[-1])

print(type(people))
print(type(states))

print(states.get('FL', 'Not Found'))
print(states.get('NY', 'Not Found'))

print(states.keys())
print(states.values())

states['FL'] = 'Florida'
print(states)

user = {'name': 'matan', 'height': 70, 'shoe size': 10.5, 'hair': 'black', 'eyes': 'blue'}

blog_post = {'title': 'the best language over the world', 'day': 'the first day'}

print(user['name'])
print(blog_post['title'])

# dictionary and lists can be inside of each other

animal_sounds = {
    "cat": ["meow", "purr"],
    "dog": ["woof", "bark"],
    "fox": []
}

matan = {'name': 'matan', 'height': 70, 'shoe size': 10.5, 'hair': 'black', 'eyes': 'blue'}
chris = {'name': 'chris', 'height': 67, 'shoe size': 10, 'hair': 'brown', 'eyes': 'blue'}
sarah = {'name': 'sarah', 'height': 61, 'shoe size': 8, 'hair': 'black', 'eyes': 'black'}

people = [matan, chris, sarah]
print(people)

for person in people:
    # print(person.get('height', 'none'))
    print(person['height'])