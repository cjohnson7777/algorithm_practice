

def welcome():
    print("Welcome to The Hundred Acre Wood!")

def greeting(name):
    print(f"Welcome to The Hundred Acre Wood {name}! My name is Christopher Robin.")

# greeting("Christina")

def print_catchphrase(character):
    if character == "Pooh":
        print("Oh bother!")
    elif character == "Tigger":
        print("TTFN: Ta-ta for now!")
    elif character == "Eeyore":
        print("Thanks for noticing me.")
    elif character == "Christopher Robin":
        print("Silly old bear.")
    else:
        print(f"Sorry! I don't know {character}'s catchphrase!")

# print_catchphrase("Iron man")

def get_item(items, index):
    if index >= len(items):
        return None
    else:
        return items[index]

# items = ["piglet", "pooh", "roo", "rabbit"]
# x = 4
# print(get_item(items, x))

def sum_honey(hunny_jars):
    honey = 0

    for num in hunny_jars:
        honey += num

    return honey
	
hunny_jars = [2, 3, 4, 5]
#print(sum_honey(hunny_jars))


def doubled(hunny_jars):
	return [num*2 for num in hunny_jars]

# hunny_jars = [1, 2, 3]
# print(doubled(hunny_jars))

def count_less_than(race_time, threshold):
    count = 0
    for t in race_time:
        if t < threshold:
            count += 1
    return count


race_time = [1, 2, 3, 4, 5, 6]
threshold = 4
count_less_than(race_time, threshold)

def print_todo_list(tasks):
    print("Pooh's To Dos:")
    for idx, task in enumerate(tasks, start=1):
        print(f"{idx}. {task}")

task = ["Count all the bees in the hive", "Chase all the clouds from the sky", "Think", "Stoutness Exercises"]
#print_todo_list(task)        

def can_pair(item_quantities):
    return all(q % 2 == 0 for q in item_quantities)

item_quantities = [2, 4, 6, 8]
#print(can_pair(item_quantities))

import math


def split_haycorns(quantity):
    divisors = []
    for i in range(1, int(math.isqrt(quantity)) + 1):
        if quantity % i == 0:
            divisors.append(i)
            other = quantity // i
            if other != i:
                divisors.append(other)
    return sorted(divisors)

def tiggerfy(s):
    forbidden = set('tiger')
    return ''.join(c for c in s if c.lower() not in forbidden)

#s = "suspicerous"
#print(tiggerfy(s))

def locate_thistles(items):
    return [i for i, item in enumerate(items) if item == "thistle"]

items = ["thistle", "stick", "carrot", "thistle", "eeyore's tail"]
#print(locate_thistles(items))



