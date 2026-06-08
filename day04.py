word1 = 'Thirty'
word2 = 'Days'
word3 = 'Of'
word4 = 'Python'
full_word = word1 + word2 + word3 + word4
print(full_word)
print(len(full_word))

company = "Coding For All"
print(company)
print(len(company))
print(company.upper())
print(company.lower())
print(company.capitalize())
print(company.title())
print(company.swapcase())
print(company[0:6])
print(company.find('Coding'))
print('Coding' in company)
print(company.replace('Coding For All','Python'))
print(company.split(' '))

companies = 'Facebook, Google, Microsoft, Apple, IBM, Oracle'
print(companies.split(','))
print(company[0])
print(company[13])
print(company[10])

word = 'Coding For All'
print(word.find('C'))
print(word.find('F'))
print(word.rfind('I'))

sentence = 'You cannot end a sentence with because because because is a conjunction'
print(sentence.find('because'))
start = sentence.index('because')
end = start + len('because because because')
print(sentence[start:end])

print(word.startswith('Coding'))
print(word.endswith('Coding'))

coding = '   Coding For All      '
print(coding.strip())

var1 = '30DaysOfPython'
var2 = 'thirty_days_of_python'
print(var1.isidentifier())
print(var2.isidentifier())

libraries = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
result = '# '.join(libraries)
print(result)

print('I am enjoying this challenge.\n I just wonder what is next.')
print('Name\tAge\tCountry\tCity')
print('Tanmay\t19\tIndia\tDelhi')

radius = 10
area = 3.14 * radius ** 2
result1 = 'The area of a circle with radius {} is {} meters sqaure'.format(radius,area)
print(result1)

a = 4
b = 3 
print('{} + {} = {}'.format(a,b,a+b))
print('{} - {} = {}'.format(a,b,a-b))
print('{} * {} = {}'.format(a,b,a*b))
print('{} / {} = {}'.format(a,b,a/b))
print('{} % {} = {}'.format(a,b,a%b))
print('{} ** {} = {}'.format(a,b,a**b))
