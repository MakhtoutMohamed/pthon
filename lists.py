the_count = [1, 2, 3, 4, 5]
stocks = ["Appel", "google", "TESLA"]
random_things = ["Puppies", 55, "Anthony Jonh", 1/2, ["Oh", "yes", "list inside a list"]]

for number in the_count:
    print("this is the count", number)

for stock in stocks:
    print("stock ticker", stock)

for random in random_things:
    print("random things:", random)


people = []

people.append("sarah")
people.append("same")
people.append("johnah")

print(people)

people.remove("johnah")
print(people)

for person in people:
    print("person is:", person)