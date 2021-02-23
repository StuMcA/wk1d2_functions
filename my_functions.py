def greet(name, time_of_day):
    return "Good " + time_of_day + ", " + name + "!"

name_1 = "Stuart"
time_of_day_1 = "afternoon"

greeting = greet(name_1, time_of_day_1)
print(greeting)

name_2 = "Sophie"
time_of_day_2 = "evening"

greeting = greet(name_2, time_of_day_2)
print(greeting)

chickens = [
    {"name": "Margaret", "age": 2, "eggs": 0 },
    {"name": "Sophie", "age": 3, "eggs": 5 },
    {"name": "The Queen", "age": 99, "eggs": 6 },
    {"name": "Steve", "age": 4, "eggs": 0 },
    {"name": "Henrietta", "age": 7, "eggs": 6000 },
]
def count_eggs(list):
    total_eggs = 0

    for bird in list:
        total_eggs += bird["eggs"]
        bird["eggs"] = 0

    return f"{total_eggs} eggs collected"

print(count_eggs(chickens))