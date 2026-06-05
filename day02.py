#LEVEL-1

first_name='Tanmay'
last_name='Jain'
full_name='Tanmay Jain'
country='India'
city='Delhi'
age=19
year=2026
is_married = False
first_name,last_name,full_name,country,city,age,year,is_married = 'Tanmay','Jain','Tanmay Jain','India','Delhi',19,2026,False

print('first name:', first_name)
print('last name:',last_name)
print("full name:",full_name)
print("country:",country)
print('city:',city)
print('year:',year)
print('Married:',is_married)
print(first_name,last_name,full_name,country,city,age,year,is_married)

#LEVEL-2

print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type((first_name,last_name,full_name,country,city,age,year,is_married)))

len_first = len(first_name)
len_last = len(last_name)
print(f"The first name {first_name} has {len_first} characters")
print(f"The last name {last_name} has {len_last} characters")
if len_first > len_last:
    print(f"Then the first name {first_name} is longer")
elif len_last > len_first:
    print(f"Then the last name {last_name} is longer")
else:
    print(f"Both have same characters")


num_one = 5
num_two = 4
total = num_one + num_two
print(total)
diff = num_one - num_two
print(diff)
product = num_one * num_two
print(product)
division = num_one / num_two
print(division)
remainder = num_one % num_two
print(remainder)
exponential = num_one ** num_two
print(exponential)
floor_division = num_one // num_two
print(floor_division)

radius = 30
area = 3.14 * radius **2
print("The area of circle is :",area)
circumference = 2 * 3.14 *radius
print("The circumference of the circle is :",circumference)
radius = int(input("Radius :"))
area = 3.14 * radius **2
print("The area of circle is :",area)

