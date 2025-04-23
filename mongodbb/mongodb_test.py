# # # # import pymongo

# # # # # myclient = pymongo.MongoClient("mongodb://localhost:27017")
# # # # myclient = pymongo.MongoClient("mongodb+srv://*****:*****@cluster0.jjj6v13.mongodb.net/node-app?retryWrites=true&w=majority&appName=Cluster0")

# # # # mydb = myclient["node-app"]
# # # # mycollection=mydb["products"]

# # # # # # print(myclient.list_database_names())
# # # # # product={"name":"Samsung S5","price":2000}

# # # # # result=mycollection.insert_one(product)

# # # # productList = [
# # # #     {"name":"Samsung S6", "price": 3000, "description":"iyi telefon"},
# # # #     {"name":"Samsung S7", "price": 4000, "categories": ['telefon','elektronik']}
# # # # ]

# # # # result=mycollection.insert_many(productList)

# # # # print(result)


# # # import pymongo

# # # # myclient = pymongo.MongoClient("mongodb://localhost:27017")
# # # # myclient = pymongo.MongoClient("mongodb+srv://*****:*****@cluster0.jjj6v13.mongodb.net/node-app?retryWrites=true&w=majority&appName=Cluster0")

# # # mydb = myclient["node-app"]
# # # mycollection=mydb["products"]

# # # # result = mycollection.find_one()
# # # for i in mycollection.find({},{"_id":0 ,"name": 1}):#id gelmez 0 name gelir 1
# # # # for i in mycollection.find({},{"_id":0 }):#id gelmez 0 name gelir 1

# # #     print(i)

# # # # print(result)



# # import pymongo
# # from bson.objectid import ObjectId

# # # myclient = pymongo.MongoClient("mongodb://localhost:27017")
# # # # myclient = pymongo.MongoClient("mongodb+srv://*****:*****@cluster0.jjj6v13.mongodb.net/node-app?retryWrites=true&w=majority&appName=Cluster0")

# # mydb = myclient["node-app"]
# # mycollection = mydb["products"]

# # # result = mycollection.find_one({"name": "Samsung S5"})
# # # result = mycollection.find_one({"_id": ObjectId("5d6a54e42afaa1169e4b9a0c")})

# # # result = mycollection.find({
# # #     "name": {
# # #         "$in" : ["Samsung S5","Samsung S6"] #eşitlik
# # #     }
# # # })

# # # result = mycollection.find({
# # #     "price": {
# # #         "$gt": 2000 # bu değerden büyük kayıtlar
# # #     }
# # # })

# # # result = mycollection.find({
# # #     "price": {
# # #         "$gte": 2000 #bu değerden büyük ve eşit kayıtlar
# # #     }
# # # })

# # # result = mycollection.find({
# # #     "price": {
# # #         "$eq": 2000  #eşitlik
# # #     }
# # # })

# # # result = mycollection.find({
# # #     "price": {
# # #         "$lte": 2000 #değerden küçük değerler
# # #     }
# # # })

# # # result = mycollection.find({
# # #     "name": { "$regex": "^S" } # S ile başlayanları getirir.
# # # })


# # for i in result:
# #     print(i)


# # import pymongo
# # from bson.objectid import ObjectId

# # # myclient = pymongo.MongoClient("mongodb://localhost:27017")
# # # # myclient = pymongo.MongoClient("mongodb+srv://*****:*****@cluster0.jjj6v13.mongodb.net/node-app?retryWrites=true&w=majority&appName=Cluster0")

# # mydb = myclient["node-app"]
# # mycollection = mydb["products"]

# # # result = mycollection.find().sort('name', -1)# -1 azalan şekilde ,1 artan şekilde
# # result = mycollection.find().sort('price', -1)
# # # result = mycollection.find().sort([('name',1), ('price',-1)])

# # for i in result:
# #     print(i)


# import pymongo
# from bson.objectid import ObjectId

# # myclient = pymongo.MongoClient("mongodb://localhost:27017")
# # # # myclient = pymongo.MongoClient("mongodb+srv://*****:*****@cluster0.jjj6v13.mongodb.net/node-app?retryWrites=true&w=majority&appName=Cluster0")

# mydb = myclient["node-app"]
# mycollection = mydb["products"]

# for i in mycollection.find():
#     print(i)

# # mycollection.update_one(
# #     {'name': 'Samsung S6'}, 
# #     {'$set': {
# #         'name': 'IPhone 7',
# #         'price': 5000
# #     }}    
# # )
# query = {'name': 'Samsung S7'}

# newvalues = {'$set': {
#                 'name': 'IPhone 8',
#                 'price': 5000
#             }} 

# result = mycollection.update_many(query, newvalues)

# print(f'{result.modified_count} adet kayıt güncellendi.')

# for i in mycollection.find():
#     print(i)


import pymongo
from bson.objectid import ObjectId

# myclient = pymongo.MongoClient("mongodb://localhost:27017")
myclient = pymongo.MongoClient("mongodb+srv://*****:*****@cluster0.jjj6v13.mongodb.net/node-app?retryWrites=true&w=majority&appName=Cluster0")

mydb = myclient["node-app"]
mycollection = mydb["products"]

for i in mycollection.find():
    print(i)

print('*'*50)

mycollection.delete_one({"name":"IPhone 8"})
# mycollection.delete_many({"name": {"$regex":"^S"}})
# result = mycollection.delete_many({})

# print(f'{result.deleted_count} adet kayıt silindi.')

for i in mycollection.find():
    print(i)