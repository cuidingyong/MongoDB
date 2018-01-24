from pymongo import MongoClient

#连接数据库
client = MongoClient('mongodb://118.31.19.120:27017/')
#查看所有的数据库
print(client.database_names())
#连接数据库 node_club_dev
db = client.get_database('node_club_dev')
#查看所有的数据表
collections = db.collection_names()
print(collections)
# 连接数据表users
users = db.get_collection('users')
# print(users.find())
# 查看某一条数据
print(users.find_one({"loginname" : "krystal"}))
#更新这条数据
users.find_one_and_update({"loginname" : "krystal"},{'$set':{"active" : True}})




