"""
Task 10
"""
#Task 1
num = input("Enter a number: ")

if num < '0':
    print(f"Number {num} Is Not Larger Than 0")
else:
    num = int(num) - 1
    count = 0
    while num > 0:
        if '6' not in str(num):
            print(num)
            count += 1
        num -= 1
    print(f"{count} Numbers Printed Successfully.")
print("-" * 20)


#Task 2
friends = ["Mohamed", "Shady", "ahmed", "eman", "Sherif"]

index = 0
ignored = 0

while index < len(friends):
    if friends[index][0].islower():
        ignored += 1
    else:
        print(friends[index])
    index += 1

print(f"Friends Printed And Ignored Names Count Is {ignored}")

print("-" * 20)


#Task 3
skills = ["HTML", "CSS", "JavaScript", "PHP", "Python"]

while skills: print(f'"{skills.pop(0)}"')

print("-" * 20)

#Task 4
my_friends = []  
max_friends = 4  

while len(my_friends) < max_friends:
    name = input("Enter your friend name: ").strip()  
    
    if name.isupper():
        print("Invalid Name")
    elif name.islower():
        name = name.capitalize()
        my_friends.append(name)
        print(f"Friend {name} Added the 1st Letter Become Capital")
        print(f"Names Left in List Is {max_friends - len(my_friends)}")
    else:
        my_friends.append(name)
        print(f"Friend {name} Added")
        print(f"Names Left in List Is {max_friends - len(my_friends)}")

print("The list is completed:", my_friends)
