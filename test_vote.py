import mongapi

def vote(get_code, ls_name):
	client = MongoClient(MONGOLAB_URI)
	db = client.get_default_database()
	votes = db['votes']

	votes.insert({"code":str(get_code),
				  "president":str(get_president),
				  "vice_president":str(get_vice_president),
				  "secretary":str(get_secretary),
				  "treasurer":str(get_treas),
				  "sports":str(get_sports),
				  "media":str(get_media),
				  "pr":str(get_pr),
				  "welf":str(get_welf),
				  "cul":str(get_cul),
				  })


if __name__=="__main__":
	ls_cand_names = [cand["name"] for cand in mongapi.get_all_candidates() if cand["name"]!=""]

	

	for cand_name in ls_cand_names:
		print cand_name