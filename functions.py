
def greet(name):
    return f"Hey {name}!"

def concatenate(word_one, word_two):
    return word_one + word_two

def age_on_dog_years(age):
    result = age * 7
    return result

print(greet('matan'))
print(greet('chris'))

print(concatenate('matan ', 'chris'))

print(age_on_dog_years(28))

name = "sloooda"

def print_different_name():
    name = 'jooohn'
    print(name)

print(name)
print_different_name()
print(name)