import csv

def find_cand(cand_map, name):
	for cand_id in cand_map:
		cand_name = cand_map[cand_id]
		if name==cand_name:
			return cand_id
	return None

def create_nominations(nominations, cand_map):
	"""
	returns dict nominations:
		{
			position 	: Position
			desc 		: Description
		}
	"""

	nom_map = dict()
	id_counter = 1
	PREFIX = "NOM"

	for nom in nominations:
		position = nom["Position"]
		nom_id = PREFIX + str(id_counter)

		if nom_id not in nom_map.keys():

			# init nomination
			nom_obj = dict()
			nom_obj["cand_id"] = find_cand(cand_map, nom["Name"])
			nom_obj["position"] = position
			nom_obj["manifesto"] = nom["What will you do if you get elected? (Manifesto)"]
			nom_obj["desc"] = nom["Your Description"]

			# add nomination to nomination hash map			
			nom_map[nom_id] = nom_obj

			# make sure id is unique
			id_counter += 1

	return nom_map

def create_candidate_photos():
	cand_photos = {}
	with open("candidate-photos.csv") as photos_file:
		cand_photos_reader = csv.DictReader(photos_file,
											delimiter=",",
											dialect="excel")
		for row in cand_photos_reader:
			cand_photos[row['CANDIDATE']] = row['PHOTO LINK']

	return cand_photos

def create_candidates(nominations):
	"""
	returns dict candidates:
	{
		cand_id	: Name
	}
	"""
	cand_map = dict()
	id_counter = 1
	PREFIX = "CAND"

	for cand in nominations:
		cand_name = cand["Name"]
		cand_id = PREFIX + str(id_counter)

		if cand_name not in cand_map.values():
			cand_map[cand_id] = cand_name

			# make sure unique
			id_counter += 1

	return cand_map

def get_nominations():
	nominations = []
	with open("nominated-candidates.csv", "rb") as nominated_file:
		nominated_reader = csv.DictReader(nominated_file, 
										delimiter=",",
										dialect="excel")
		for row in nominated_reader:
			print row
			nominations.append(row)	

	cand_map = create_candidates(nominations)
	nom_map = create_nominations(nominations, cand_map)

	return nom_map

def get_candidates():
	nominations = []
	with open("nominated-candidates.csv", "rb") as nominated_file:
		nominated_reader = csv.DictReader(nominated_file, 
										delimiter=",",
										dialect="excel")
		for row in nominated_reader:
			nominations.append(row)	

	cand_map = create_candidates(nominations)
	
	return cand_map

def get_cand_photos():
	return create_candidate_photos()

def print_pretty_nom(nom_map, cand_map):
	print "==="*30
	count = 1
	for nom_id in nom_map.keys():
		nom = nom_map[nom_id]
		print "---"*30
		print "No: ", count
		print "nom_id: ", nom_id
		print "candidate name: ", cand_map[nom["cand_id"]]
		print "Description: ", "\n",  nom["desc"]
		print "Manifesto: ", "\n", nom["manifesto"]
		print "Position: ", nom["position"]
		print "---"*30
		count += 1
	print "==="*30


if __name__=="__main__":

	nominations = []

	with open("nominated-candidates.csv", "rb") as nominated_file:
		nominated_reader = csv.DictReader(nominated_file, 
										delimiter=",",
										dialect="excel")
		for row in nominated_reader:
			nominations.append(row)
	
	cand_map = create_candidates(nominations)
	nom_map = create_nominations(nominations, cand_map)

	for nom_id in nom_map.keys():
		nom = nom_map[nom_id]
		print "==="*30
		print "cand_id: ", nom["cand_id"]
		print "candidate name: ", cand_map[nom["cand_id"]]
		print "Position: ", nom['position']
		print "candidate description: \n", nom['desc']
		print "candidate manifesto: \n", nom["manifesto"]
	print "==="*30

	for cand_id in cand_map.keys():
		print cand_id, cand_map[cand_id]

	# cand_photos = create_candidate_photos()
	# for cand_name in cand_photos:
	# 	print cand_name, cand_photos[cand_name]
