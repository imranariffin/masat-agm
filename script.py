import pymongo
from pymongo import MongoClient

client = MongoClient('mongodb://admin:admin@ds031581.mongolab.com:31581/heroku_app34859325')
db = client.get_default_database()

# upvotes = db['upvotes']
# cursor = upvotes.find()

# upvotes.insert({"username":"Anas Faris", "vote_id":"1550d1805e4b0578757ffaf9b"})
man = db['man']
cursor = man.find()

# for doc in cursor:
# 	print doc['_id']
# 	doc['votes'] = 0
# 	man.update({'_id':doc['_id']}, {"$set":doc}, upsert=False)

# votes = db['votes']
# cursor_votes = votes.find()

# for doc in cursor_votes:
# 	string = 'president'
# 	target = doc[string]
# 	print doc['_id'], target
# 	if target == "Nor Fatihah Ahmad":
# 		print True
		# doc[string] = "Faris Sulaiman"
		# votes.update({'_id':doc['_id']}, {"$set":doc})

for doc in cursor:
	val0 = doc['manifesto'][0]
	# man_id = "0" + str(doc['_id'])
	# val0.append(man_id)

	val1 = doc['manifesto'][1]
	# man_id = "1" + str(doc['_id'])
	# val1.append(man_id)

	val2 = doc['manifesto'][2]
	# man_id = "2" + str(doc['_id'])
	# val2.append(man_id)

	# print val0[1]
	# print val1[1]
	# print val2[1]
	
	# doc['manifesto'][0] = val0
	# doc['manifesto'][1] = val1
	# doc['manifesto'][2] = val2

	doc['manifesto'][0][1] = 0
	doc['manifesto'][1][1] = 0
	doc['manifesto'][2][1] = 0

	man.update({'_id':doc['_id']}, {"$set":doc})

client.close()