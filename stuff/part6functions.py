def doSomething(param, param3, param2='. Hello there'):
    return ('Do something' + param + param2, param)
    print('bye bye')
    # Return rules
    # 1) Only 1 value can be returned
    # 2) End the function

# def doSomething():
#     pass

def main():
    subject = ' with Tiki'
    result = doSomething(subject,'')
    # result[2] = 'lalalala'
    print(doSomething(' with someone', ' hahahahaha!'))

def somethingElse():
    print('Doing something else')
