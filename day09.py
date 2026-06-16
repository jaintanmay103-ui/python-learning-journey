# age = int(input('Enter your age :'))
# if age >= 18:
#     print('You are old enoughh to drive')
# else:
#     print(f'You need {18-age} more years to drive') 

# my_age = 25
# your_age = int(input("Enter your age:"))
# difference = abs(my_age - your_age)
# if my_age > your_age:
#     if difference == 1:
#         print(f"I am {difference} year older than you.")
#     else:
#         print(f"I am {difference} years older than you.")
# elif your_age > my_age:
#     if difference == 1:
#         print(f"You are {difference} year older than me.")
#     else:
#         print(f"You are {difference} years older than me.")
# else:
#     print("We are the same age.")


# a = int(input("Enter a number between 1 to 10:"))
# b = int(input("Enter a number between 1 to 10:"))
# if a > b:
#     print(f"{a} is greater than {b}")
# elif b > a:
#     print(f"{b} is greater than {a}")
# else:
#     print(f"{a} is equal to {b}")


# score = int(input("Enter student's score: "))

# if 90 <= score <= 100:
#     print("Grade: A")
# elif 80 <= score <= 89:
#     print("Grade: B")
# elif 70 <= score <= 79:
#     print("Grade: C")
# elif 60 <= score <= 69:
#     print("Grade: D")
# elif 0 <= score <= 59:
#     print("Grade: F")
# else:
#     print("Invalid score")

# month = input("Enter a month: ").capitalize()

# if month in ["September", "October", "November"]:
#     print("Season: Autumn")

# elif month in ["December", "January", "February"]:
#     print("Season: Winter")

# elif month in ["March", "April", "May"]:
#     print("Season: Spring")

# elif month in ["June", "July", "August"]:
#     print("Season: Summer")

# else:
#     print("Invalid month")

# fruits = ['banana', 'orange', 'mango', 'lemon']
# fruit = input("Enter a fruit:").strip().lower()
# if fruit in fruits:
#     print("That fruit already exist in the list")
# else:
#     fruits.append(fruit)
#     print("Modified List:",fruits)


person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}

# Middle skill
if 'skills' in person:
    skills = person['skills']
    print("Middle skill:", skills[len(skills) // 2])

# Python skill
if 'Python' in person['skills']:
    print("Person has Python skill")

# Developer title
skills = person['skills']

if skills == ['JavaScript', 'React']:
    print("He is a front end developer")
elif all(skill in skills for skill in ['Node', 'Python', 'MongoDB']):
    print("He is a backend developer")
elif all(skill in skills for skill in ['React', 'Node', 'MongoDB']):
    print("He is a fullstack developer")
else:
    print("unknown title")

# Marriage and country
if person['is_married'] and person['country'] == 'Finland':
    print(
        f"{person['first_name']} {person['last_name']} lives in "
        f"{person['country']}. He is married."
    )
