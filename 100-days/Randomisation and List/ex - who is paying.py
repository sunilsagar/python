import random

name_string = input("Give me everybody's names, separated by comma.\n")
names = name_string.split(",")

#print(names[0])
num_items = len(names)

random_choice = random.randint(0, num_items - 1 )
print(random_choice)

person_to_pay = names[random_choice]
print(person_to_pay)

## Short Code:
person_to_pay = random.choice(names)
print(person_to_pay)