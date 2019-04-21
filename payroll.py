quit = False
userInput = None
employeeList = dict()

#Payroll calculation variables
hours = 0.0
gross = 0.0
tax = 0.0
nett = 0.0
taxRate = 0.18
otRate = 1.5
regHours = 40
basicPay = 10

#while not quit:
while not quit:
    print('MAIN MENU:')
    print('1 - Enter new employee')
    print('2 - Calculate pay')
    print('3 - List employees')
    print('x - Quit')

    userInput = input('Enter Selection: ')
    if userInput == '1':
        userInput = None
        userInput = input('Enter Name: ')
        employeeList[userInput] = (0.0,0.0,0.0)
    elif userInput == '2':
        userInput = None
        userInput = input('For which employee: ')
        result = employeeList.get(userInput,'No such employee')

        if result != 'No such employee':
            hours = float(input('Enter # of hours worked: '))

            if hours > regHours:
                gross = ((hours - regHours) * otRate * basicPay) + (regHours * basicPay)
            else:
                gross = hours * basicPay

            tax = gross * taxRate
            nett = gross - tax

            employeeList[userInput] = (gross,tax,nett)

    elif userInput == '3':
        print('Employee List:')
        nameList = list(employeeList.keys())
        nameList.sort()
        for name in nameList:
            print ('{} => {}'.format(name, employeeList[name][2]))
    elif userInput == 'x':
        quit = True
    else:
        print('Invalid entry!')