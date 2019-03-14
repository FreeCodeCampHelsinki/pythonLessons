# print('Hello world')

# This is a comment

strObj ="This is a string object"
num = 210
sentence = "This is a string."
# "This is going to be very long"
sentence2 = 'This is also a string'
sentence3 = '''This is a multiline string.
This is going to be a really long sentence.'''
print("Tiki's word is \"Hello\" ")
# pep8.org -> Python Style guide
print(strObj.format())
print(sentence + sentence2 + str(num) )
print("Tiki is mentally {1}{2} years old. {0}".format(6,'And he is dellusional.',"Another item"))

print("-"*50)
myStr = "The quick brown fox jumps over the lazy dog"
print(myStr[-3:])