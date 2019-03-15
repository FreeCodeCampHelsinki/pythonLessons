mySet = {'Giovanni','Tero','Lars','Vullnet'}
otherSet ={}
mySet.add('Jemal')
mySet.add('Tero')
myList = list(mySet)
myList.sort()
print(len(myList))
print(mySet)
print(myList)
print('-'*50)

myDictionary = {'key':'value','name':'Tiki'}
#myDictionary = dict()
countries = {
    'fi':'Finland'
    ,'my':{'name':'Malaysia','population':30000000,'land_mass':300000}
    ,'it':'Italy'
    ,'al':'Albania'
    ,'de':'Germany'
    ,'au':'Australia'
    ,'ja':'Jamaica'
    ,'ua':'Ukraine'
    ,'ru':'Russia'
    ,'et':'Ethiopia'
}

countries['cn'] = 'China'

countries['cn'] = 'People\'s Republic of China'

#del countries['my']

print(countries['my']['name'])
print(countries.get('Finland','Country not found!'))