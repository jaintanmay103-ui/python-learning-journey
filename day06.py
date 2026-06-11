empty_tuple = ()
print(empty_tuple)

brothers = ('Khushal','Tanmay','Manvik')
sisters = ('Pihu','Mitika')
siblings = brothers + sisters
print(siblings)
print(len(siblings))
siblings = list(siblings)
siblings.append('Rohan')
siblings.append('Shreya')
print(siblings)
family_members = tuple(siblings)
print(family_members)

*siblings, father, mother = family_members
print("Siblings:", siblings)
print("Father:", father)
print("Mother:", mother)

fruits = ('apple', 'banana', 'cherry')
vegetables = ('potato', 'tomato', 'onion')
animal_products = ('milk', 'butter', 'cheese')
food_stuff = fruits + vegetables + animal_products 
print(food_stuff)
food_stuff = list(food_stuff)
print(food_stuff)
print(food_stuff[4:5])
print(food_stuff[:3])
print(food_stuff[-3:])
food_stuff = tuple(food_stuff)
del food_stuff

