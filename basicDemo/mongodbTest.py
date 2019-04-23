import pymongo
import json


mongoClient = pymongo.MongoClient('mongodb://localhost:27017/')

dblist = mongoClient.list_database_names()

# if not('python' in dblist):
#     print('python inexistence')
#     mongoClient['python']

pythondb = mongoClient['python']

# collist = pythondb.list_collection_names()
# if 'users' in collist:
#     print('users 集合已存在')

users = pythondb['users']

mydict = { "name": "RUNOOB", "alexa": "10000", "url": "https://www.runoob.com" }

# add
# x = users.insert_one(mydict)
# print(x.inserted_id)

# print(x) 
# <pymongo.results.InsertOneResult object at 0x104fc92c8>

# delete
# users.delete_one({'name':'RUNOOB'})
# x = users.delete_many({'name':'RUNOOB'})
# print(x.deleted_count)




# 自增id
# create count collection
counters = pythondb['counters']
# counters.insert_one({'_id':'orderid', 'sequence_value':0})

# 此方法只返回操作结果
# doc = counters.update_one({'_id':'orderid'}, {'$inc':{'sequence_value':1}})

# 以字典方式返回修改后的新值
# doc = counters.find_one_and_update({'_id':'orderid'}, {'$inc':{'sequence_value':1}})
# print(str(doc))
# print(type(doc))



def getNextSquenceValue(sequenceName):
    query = {'_id':sequenceName}
    update = {"$inc":{"sequence_value":1}}
    sequenceDocument = counters.find_one_and_update(query, update)
    return sequenceDocument['sequence_value']

# newId = getNextSquenceValue('userid')
# print(newId)

userList = [
    {'name': 'huahua'},
    {'name': 'sansan'},
    {'name': 'susu'}
]

for user in userList:
    user.update({'_id':getNextSquenceValue('userid')})
    ur = users.insert_one(user)
    print(ur.inserted_id)

print(str(userList))    

 