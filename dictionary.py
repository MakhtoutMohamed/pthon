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