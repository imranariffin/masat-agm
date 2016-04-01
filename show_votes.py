from mongapi import get_all_votes

def show_count(votes):
	pr_count = {}


if __name__=="__main__":
	for vote in get_all_votes():
		print vote['code']
		for key in vote.keys():
			if key != "code" and key != '_id':
				print "\t", key, vote[key]

	print "\nshowing count:\n"

	president_count = {}
	vice_president_count = {}
	sec_count = {}
	treas_count = {}
	sports_count = {}
	media_count = {}
	welf_count = {}
	cul_count = {}
	pr_count = {}

	for doc in get_all_votes():
		try:
			if doc['president'] not in president_count:
				president_count[doc['president']] = 1
			else:
				president_count[doc['president']] += 1

			if doc['vice_president'] not in vice_president_count:
				vice_president_count[doc['vice_president']] = 1
			else:
				vice_president_count[doc['vice_president']] += 1

			if doc['secretary'] not in sec_count:
				sec_count[doc['secretary']] = 1
			else:
				sec_count[doc['secretary']] += 1

			if doc['treasurer'] not in treas_count:
				treas_count[doc['treasurer']] = 1
			else:
				treas_count[doc['treasurer']] += 1

			if doc['sports'] not in sports_count:
				sports_count[doc['sports']] = 1
			else:
				sports_count[doc['sports']] += 1

			if doc['media'] not in media_count:
				media_count[doc['media']] = 1
			else:
				media_count[doc['media']] += 1

			if doc['pr'] not in pr_count:
				pr_count[doc['pr']] = 1
			else:
				pr_count[doc['pr']] += 1

			if doc['cul'] not in cul_count:
				cul_count[doc['cul']] = 1
			else:
				cul_count[doc['cul']] += 1

			if doc['welf'] not in welf_count:
				welf_count[doc['welf']] = 1
			else:
				welf_count[doc['yrep4']] += 1

			# if doc['yrep3'] not in yrep3_count:
			# 	yrep3_count[doc['yrep3']] = 1
			# else:
			# 	yrep3_count[doc['yrep3']] += 1

			# if doc['yrep2'] not in yrep2_count:
			# 	yrep2_count[doc['yrep2']] = 1
			# else:
			# 	yrep2_count[doc['yrep2']] += 1
		except:
			print "problem"

		# try:
		# 	s = doc['secretary']
		# 	if s not in secretary_count:
		# 		secretary_count[s] = 1
		# 	else:
		# 		secretary_count[s] += 1
		# except:
		# 	pass

	pc = []
	vpc = []
	sc = []
	treas = []
	sports = []
	media = []
	cul = []
	welf = []
	pr = []

	for key in president_count:
		pc.append([key, president_count[key]])
	for key in vice_president_count:
		vpc.append([key, vice_president_count[key]])
	for key in sec_count:
		sc.append([key, sec_count[key]])
	for key in treas_count:
		treas.append([key, treas_count[key]])
	for key in sports_count:
		sports.append([key, sports_count[key]])
	for key in media_count:
		media.append([key, media_count[key]])
	for key in cul_count:
		cul.append([key, cul_count[key]])
	for key in pr_count:
		pr.append([key, pr_count[key]])
	for key in welf_count:
		welf.append([key, welf_count[key]])

	full_ls = [{'position':'p','ls':pc},
			   {'position':'vp','ls':vpc},
			   {'position':'s','ls':sc},
			   {'position':'treas','ls':treas},
			   {'position':'sports','ls':sports},
			   {'position':'media','ls':media},
			   {'position':'cul','ls':cul},
			   {'position':'welf','ls':welf},
			   {'position':'pr','ls':pr}]

	for r in full_ls:
		keys = r.keys()
		print r[keys[0]]
		for ret in r[keys[1]]:
			print "\t", ret[0], ret[1]