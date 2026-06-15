dog = {
    'name': 'Buddy',
    'color': 'Brown',
    'breed': 'Labrador',
    'legs': 4,
    'age': 3
}

student = {
    'first_name': 'Tanmay',
    'last_name': 'Jain',
    'gender': 'male',
    'age': 19,
    'marital_status': 'single',
    'skills': ['Python', 'JavaScript', 'HTML', 'CSS'],
    'country': 'India',
    'city': 'Delhi',
    'address': '123 Main Street'
}
print(len(student))
Skills = student['skills']
print(Skills)
print(type(Skills))
student['skills'].append('React')
print(student)
keys = student.keys()
print(keys)
values = student.values()
print(values)
print(student.items())
student.popitem()
print(student)
del dog
