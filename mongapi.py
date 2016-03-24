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

def get_all_candidates():
	# set up db
	client = MongoClient(MONGOLAB_URI)
	db = client.get_default_database()
	cand_collection = db['candidates']

	candidates = []

	for cand in cand_collection.find():
		candidates.append(cand)

	return candidates

def get_all_nominations():
	# set up db
	client = MongoClient(MONGOLAB_URI)
	db = client.get_default_database()
	nom_collection = db['nominations']

	nominations = []

	for nom in nom_collection.find():
		nominations.append(nom)

	return nominations

def delete_all_candidates():
	"""
	!!!!	WARNING THINK TWICE BEFORE USING THIS 	!!!!!
	"""
	# set up db
	client = MongoClient(MONGOLAB_URI)
	db = client.get_default_database()
	cand_collection = db['candidates']

	for cand in cand_collection.find():
		cand_collection.delete_one({"_id" : cand["_id"]})

def delete_all_nominations():
	"""
	!!!!	WARNING THINK TWICE BEFORE USING THIS 	!!!!!
	"""
	# set up db
	client = MongoClient(MONGOLAB_URI)
	db = client.get_default_database()
	nom_collection = db['nominations']

	for nom in nom_collection.find():
		nom_collection.delete_one({"_id" : nom["_id"]})

if __name__=="__main__":

	nom_map = {nom["nom_id"] : nom for nom in get_all_nominations()}
	# print get_all_nominations()[0]
	cand_map = {cand["cand_id"] : cand for cand in get_all_candidates()}
	# print cand_map
	readcsv.print_pretty_nom(nom_map, cand_map)
