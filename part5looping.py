counter = 0
while counter < 5:
    print('Hello')
    counter += 1 # counter = counter + 1
    if counter == 3:
        # break
        continue
    print("Let's do this again")

print('End of the program')
print('='*50)

for whatever in range(1,10,2):
    print(whatever)

# names = ['Peter','Paul','Mary']
# names = ('Peter','Paul','Mary')
# names = {'Peter','Paul','Mary'}
names = {'pete':'Peter','paulie':'Paul','mar':'Mary'}
for x in names:
    #print(name,end=',')
    print(names[x],end=',')
    #print(names)

print('='*50)

userInput = input('please enter something:')
print(userInput)