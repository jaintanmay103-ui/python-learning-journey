it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
print(len(it_companies))
it_companies.add('Twitter')
print(it_companies)
IT_companies = {'Spotify','Minecraft'}
it_companies.update(IT_companies)
print(it_companies)
it_companies.remove('Minecraft')
print(it_companies)



A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
print(A.union(B))
print(A.intersection(B))
print(A.issubset(B))
print(A.union(B))
print(B.union(A))
print(A.symmetric_difference(B))
del A
del B


age = [22, 19, 24, 25, 26, 24, 25, 24]
age_set = set(age)
print(len(age_set))
print(len(age))
print(len(age) > len(age_set))


sentence = 'I am a teacher and I love to inspire and teach people'
words = sentence.split()
unique_words = set(words)
print(unique_words)
print('Number of unique words:',len(unique_words))

