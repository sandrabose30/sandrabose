import pymongo

client = pymongo.MongoClient()


mydb = client["mydatabase"]

print(client.list_database_names())


mycol = mydb["people"]


mydict = { "name": "John", "address": "Highway 37" }
x = mycol.insert_one(mydict)


print(x.inserted_id)

mylist = [
  { "name": "Jane", "age":40},
  { "name": "Mark"}
  ]
x = mycol.insert_many(mylist)


print(x.inserted_ids)


print(client.list_database_names())


print(mydb.list_collection_names())


print(mycol.find_one())


for x in mycol.find():
  print(x)


for x in mycol.find({},{ "address": 0 }):
  print(x)


for x in mycol.find({"Name":"Jane}):
  print(x)