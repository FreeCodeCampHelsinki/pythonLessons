myStr = str("Hello {}")

print(myStr.format("Tiki"))

myInt = int(4)
myInt = 4

myList = ["Apples","Pears","Bananas",'Grapes',"Durians"]
'''myList = list()
sd;lfasdsa;lambda
;ldsafdsa;lk
kjsdflakf'''
myList.append("Rambutans")
#myList.sort()
myList.reverse()
myList.insert(2,"Pears")
myList[3] = "Cherries"
fruitIndex = myList.index("Pears",4)
myList[fruitIndex] = "Manggoes"
myList.remove("Rambutans")
del myList[-1]
print(myList)
#print(myList.index("Blah"))

print("-"*50)

myTuple = ('Tiki Shabudin',46,"I'm hungry")
print(myTuple.index(46))
print(myTuple[0])
#myTuple = tuple()

myTuple = ("Tikriti Shabudin", 46, "Male",['apples','bananas'])
myTuple[3].append("whatever")
print(myTuple)

name,age,gender,fav_fruits = myTuple
myTuple = (name,age,gender)
print(myTuple)
