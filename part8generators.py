import sys
import random

def lottoGen(digits):
    for number in range(digits):
        yield random.randint(0,9)

result = ''
for num in lottoGen(7):
    result += str(num)

print(result)

def fixedGen():
    yield 'A'
    yield 'B'
    yield 'C'

for y in fixedGen():
    print(y)    

def myGenerator():
    #imagine this data is coming from a db
    words = ['monkey','puppies','dork','idiot','dodo']
    for word in words:
        yield word

for whatever in myGenerator():
    print(whatever)

wordList = list(myGenerator())

print(sys.getsizeof(myGenerator()))
print(sys.getsizeof(wordList))
# numbers = list(range(0,1000))
# numbers2 = range(0,1000)

# for num in numbers2:
#     print(num)

# print(numbers)
# print(sys.getsizeof(numbers))
# print(sys.getsizeof(numbers2))