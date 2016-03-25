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

if __name__=="__main__":

	# insert_all_candidates()
	# insert_all_nominations()

	nom_map = {nom["nom_id"] : nom for nom in get_all_nominations()}
	# print get_all_nominations()[0]
	cand_map = {cand["cand_id"] : cand for cand in get_all_candidates()}
	# print cand_map
	readcsv.print_pretty_nom(nom_map, cand_map)

	for cand_id in cand_map.keys():
		print cand_id, cand_map[cand_id]

