from pymongo import MongoClient
import readcsv

try:
	from auth import MONGOLAB_URI
except ImportError:
	import os
	MONGOLAB_URI = os.environ['MONGOLAB_URI']

def insert_all_candidates():
	# set up db
	client = MongoClient(MONGOLAB_URI)
	db = client.get_default_database()
	cand_collection = db['candidates']

	# get all candidates from csvfile
	cand_map = readcsv.get_candidates()

	for cand_id in cand_map.keys():
		cand_name = cand_map[cand_id]
		print "inserting ", cand_id, cand_name

		# avoid duplicate
		if cand_collection.find_one({"cand_id" : cand_id}) == None:
			insert_id = cand_collection.insert_one({
					"cand_id" : cand_id,
					"name" : cand_name
				}).inserted_id
			print "inserted ", insert_id, " : ", cand_name
		else:
			print "err: ", cand_id, " oredy inserted"
	client.close()

def insert_all_nominations():
	# set up db
	client = MongoClient(MONGOLAB_URI)
	db = client.get_default_database()
	nom_collection = db['nominations']

	# get all nominations
	nom_map = readcsv.get_nominations()

	for nom_id in nom_map:
		nom = nom_map[nom_id]
		nom["nom_id"] = nom_id

		# avoid duplicate
		if nom_collection.find_one({"nom_id" : nom_id}) == None:			
			insert_id = nom_collection.insert_one(nom).inserted_id
			print "inserted ", nom_id
		else:
			print "err: ", nom_id ," oredy inserted"

	client.close()

def insert_all_candidate_photos():
	# set up db
	client = MongoClient(MONGOLAB_URI)
	db = client.get_default_database()
	cand_photo_collection = db['cand_photos']

	photo_map = readcsv.get_cand_photos()

	for cand_name in photo_map:
		photo_link = photo_map[cand_name]

		if cand_photo_collection.find_one({"CANDIDATE" : cand_name}) == None:
			insert_id = cand_photo_collection.insert_one({
				"CANDIDATE" : cand_name, 
				"PHOTO LINK" : photo_link
			})
			print "inserted ", photo_link
		else:
			print "err: ", photo_link, " oredy inserted"

	client.close()

def get_all_candidates():
	# set up db
	client = MongoClient(MONGOLAB_URI)
	db = client.get_default_database()
	cand_collection = db['candidates']

	candidates = []

	for cand in cand_collection.find():
		candidates.append(cand)

	client.close()
	return candidates

def get_all_nominations():
	# set up db
	client = MongoClient(MONGOLAB_URI)
	db = client.get_default_database()
	nom_collection = db['nominations']

	nominations = []

	for nom in nom_collection.find():
		nominations.append(nom)

	client.close()
	return nominations

def get_all_cand_photos():
	# set up db
	client = MongoClient(MONGOLAB_URI)
	db = client.get_default_database()
	cand_photo_collection = db['cand_photos']

	cand_photos = []

	for cand_photo in cand_photo_collection.find():
		cand_photos.append(cand_photo)

	client.close()
	return cand_photos

def get_all_votes():
	# set up db
	client = MongoClient(MONGOLAB_URI)
	db = client.get_default_database()
	vote_collection = db['votes']

	votes = [vote for vote in vote_collection.find()]
	client.close()
	return votes

def delete_all_candidates():
	"""
	!!!!	WARNING THINK TWICE BEFORE USING THIS 	!!!!!
	"""
	# set up db
	client = MongoClient(MONGOLAB_URI)
	db = client.get_default_database()
	cand_collection = db['candidates']

	print "deleting all candidates..."
	import time
	print "."
	time.sleep(1)
	print ".."
	time.sleep(1)
	print "..."
	time.sleep(1)
	print "done"

	for cand in cand_collection.find():
		cand_collection.delete_one({"_id" : cand["_id"]})

	client.close()

def delete_all_nominations():
	"""
	!!!!	WARNING THINK TWICE BEFORE USING THIS 	!!!!!
	"""
	# set up db
	client = MongoClient(MONGOLAB_URI)
	db = client.get_default_database()
	nom_collection = db['nominations']

	print "deleting all nominations..."
	import time
	print "."
	time.sleep(1)
	print ".."
	time.sleep(1)
	print "..."
	time.sleep(1)
	print "done"

	for nom in nom_collection.find():
		nom_collection.delete_one({"_id" : nom["_id"]})
	client.close()

def delete_all_cand_photos():
	"""
	!!!!	WARNING THINK TWICE BEFORE USING THIS 	!!!!!
	"""
	# set up db
	client = MongoClient(MONGOLAB_URI)
	db = client.get_default_database()
	cand_photo_collection = db['cand_photos']

	print "deleting all candidate photos..."
	import time
	print "."
	time.sleep(1)
	print ".."
	time.sleep(1)
	print "..."
	time.sleep(1)
	print "done"

	for cand_photo in cand_photo_collection.find():
		cand_photo_collection.delete_one({"_id" : cand_photo["_id"]})
	client.close()

def delete_all_questions():
	"""
	!!!!	WARNING THINK TWICE BEFORE USING THIS 	!!!!!
	"""
	# set up db
	client = MongoClient(MONGOLAB_URI)
	db = client.get_default_database()
	q_collection = db['questions']

	print "deleting all questions..."
	import time
	print "."
	time.sleep(1)
	print ".."
	time.sleep(1)
	print "..."
	time.sleep(1)
	print "done"

	for q in q_collection.find():
		q_collection.delete_one({"_id" : q["_id"]})

	client.close()

def delete_all_votes():
	"""
	!!!!	WARNING THINK TWICE BEFORE USING THIS 	!!!!!
	"""
	# set up db
	client = MongoClient(MONGOLAB_URI)
	db = client.get_default_database()
	vote_collection = db['votes']

	print "deleting all votes..."
	import time
	print "."
	time.sleep(1)
	print ".."
	time.sleep(1)
	print "..."
	time.sleep(1)
	print "done"

	for vote in vote_collection.find():
		vote_collection.delete_one({"_id" : vote["_id"]})
	client.close()

def update_candidate_photo(cand_id, img_url):
	# set up db
	client = MongoClient(MONGOLAB_URI)
	db = client.get_default_database()
	cand_collection = db['candidates']

	res = cand_collection.update_one(
		{
			"cand_id" : cand_id
		},
		{
			"$set" : {"img_url" : img_url}
		})
	print "matched_count: ", res.matched_count
	print "modified_count: ", res.modified_count
	client.close()

def insert_question(asker, question, cand_id):
	# set up db
	client = MongoClient(MONGOLAB_URI)
	db = client.get_default_database()
	q_collection = db['questions']

	insert_id = q_collection.insert_one({
			"cand_id" : cand_id,
			"question" : question,
			"asker" : asker,
			"answer" : ""
		}).inserted_id

	client.close()
	return insert_id

def get_questions():
	# set up db
	client = MongoClient(MONGOLAB_URI)
	db = client.get_default_database()
	q_collection = db['questions']

	return [q for q in q_collection.find()]

def get_cand_questions(cand_id):
	# set up db
	client = MongoClient(MONGOLAB_URI)
	db = client.get_default_database()
	q_collection = db['questions']	

	return [q for q in q_collection.find({"cand_id" : cand_id})]



if __name__=="__main__":

	delete_all_candidates()
	delete_all_nominations()
	delete_all_cand_photos()

	insert_all_candidates()
	insert_all_nominations()
	insert_all_candidate_photos()

	nom_map = {nom["nom_id"] : nom for nom in get_all_nominations()}
	cand_map = {cand["cand_id"] : cand for cand in get_all_candidates()}
	photo_map = {cand_photo['CANDIDATE'] : cand_photo['PHOTO LINK'] for cand_photo in get_all_cand_photos()}
	# print cand_map
	readcsv.print_pretty_nom(nom_map, cand_map)

	for cand_id in cand_map.keys():
		print cand_id, cand_map[cand_id]

	for cand_name in photo_map.keys():
		print cand_name, photo_map[cand_name]

