#Bottle Framework
from bottle import route, run, template, request, static_file, get, post, response, Bottle, error
import bottle
import os
import random
from bson.json_util import dumps
from helper import *

from uuid import uuid4

def eat_cookies():
	cookie_id = bottle.request.get_cookie('mycookiename', str(uuid4()))
	bottle.response.set_cookie('mycookiename', cookie_id, max_age=950400)
	return cookie_id

#specifying the path for the files
@route('/static/<filepath:path>')
def server_static(filepath):
	return static_file(filepath, root='.')

import pymongo
from pymongo import MongoClient

from bson.json_util import dumps
from bson import json_util

@route("/vote")
def man_builder():
	return template('views/closed.html',
					page="vote")

@route("/result")
def man_builder():
	return template('views/closed.html',
					page="result")

@route("/man")
def get_all_man():
	client = MongoClient('mongodb://admin:admin@ds031581.mongolab.com:31581/heroku_app34859325')
	db = client.get_default_database()
	man = db['man']
	doc = man.find()
	return dumps(doc, sort_keys=True, indent=4, default=json_util.default)

@route("/man/<vote_id>")
def get_one_man(vote_id):
	client = MongoClient('mongodb://admin:admin@ds031581.mongolab.com:31581/heroku_app34859325')
	db = client.get_default_database()
	man = db['man']
	cursor = man.find()
	target = []
	for doc in cursor:
		for e in doc['manifesto']:
			if e[2] == vote_id:
				target = doc
	return dumps(target, sort_keys=True, indent=4, default=json_util.default)

@route("/mbuilder")
def man_builder():

	return template('views/mbuilder.html',
					page="mbuilder")

@route('/ask.json')
def ask_json():
	client = MongoClient('mongodb://admin:admin@ds031581.mongolab.com:31581/heroku_app34859325')
	db = client.get_default_database()
	ask = db['ask']
	doc = ask.find()
	client.close()
	return dumps(doc, sort_keys=True, indent=4, default=json_util.default)

@route('/test')
def test():
	return template('views/test.html')

# @route('/api', method='GET')
# def get_like():
# 	client = MongoClient('mongodb://admin:admin@ds031581.mongolab.com:31581/heroku_app34859325')
# 	db = client.get_default_database()
# 	entity = db['man'].find()
# 	if not entity:
# 		abort(404, 'No document with id %s' % id)
# 	entity = dumps(entity)
# 	return entity

import httpagentparser

def browser_info():
	s = request.environ.get('HTTP_USER_AGENT')
	return httpagentparser.simple_detect(s)

@route("/slide", method="GET")
def main():
	client = MongoClient('mongodb://admin:admin@ds031581.mongolab.com:31581/heroku_app34859325')
	db = client.get_default_database()
	man = db['man']

	cursor = man.find();

	ls_pres = []
	ls_vp = []
	ls_sec = []
	ls_treas = []
	ls_sport = []
	ls_media = []
	ls_pr = []
	ls_cul = []
	ls_yrep4 = []
	ls_yrep3 = []
	ls_yrep2 = []

	for doc in cursor:
		if doc['position'] == "President":
			ls_pres.append([doc['name'],doc['comment'],doc['manifesto'],doc['_id']])
		elif doc['position'] == "VP":
			ls_vp.append([doc['name'],doc['comment'],doc['manifesto'],doc['_id']])
		elif doc['position'] == "Secretary":
			ls_sec.append([doc['name'],doc['comment'],doc['manifesto'],doc['_id']])
		elif doc['position'] == "Treasurer":
			ls_treas.append([doc['name'],doc['comment'],doc['manifesto'],doc['_id']])
		elif doc['position'] == "Sports":
			ls_sport.append([doc['name'],doc['comment'],doc['manifesto'],doc['_id']])
		elif doc['position'] == "Media":
			ls_media.append([doc['name'],doc['comment'],doc['manifesto'],doc['_id']])
		elif doc['position'] == "PR":
			ls_pr.append([doc['name'],doc['comment'],doc['manifesto'],doc['_id']])
		elif doc['position'] == "Cultural":
			ls_cul.append([doc['name'],doc['comment'],doc['manifesto'],doc['_id']])
		elif doc['position'] == "YearRep4":
			ls_yrep4.append([doc['name'],doc['comment'],doc['manifesto'],doc['_id']])
		elif doc['position'] == "YearRep3":
			ls_yrep3.append([doc['name'],doc['comment'],doc['manifesto'],doc['_id']])
		elif doc['position'] == "YearRep2":
			ls_yrep2.append([doc['name'],doc['comment'],doc['manifesto'],doc['_id']])

	random.shuffle(ls_pres)
	random.shuffle(ls_vp)
	random.shuffle(ls_sec)
	random.shuffle(ls_treas)
	random.shuffle(ls_sport)
	random.shuffle(ls_media)
	random.shuffle(ls_pr)
	random.shuffle(ls_cul)
	random.shuffle(ls_yrep4)
	random.shuffle(ls_yrep3)
	random.shuffle(ls_yrep2)

	return template('views/slide.html', ls_pres=ls_pres,
								  ls_vp=ls_vp,
								  ls_sec=ls_sec,
								  ls_treas=ls_treas,
								  ls_sport=ls_sport,
								  ls_media=ls_media,
								  ls_pr=ls_pr,
								  ls_cul=ls_cul,
								  ls_yrep4=ls_yrep4,
								  ls_yrep3=ls_yrep3,
								  ls_yrep2=ls_yrep2,
								  page="april2")

@route("/", method="GET")
def main():
	client = MongoClient('mongodb://admin:admin@ds031581.mongolab.com:31581/heroku_app34859325')
	db = client.get_default_database()
	man = db['man']

	cursor = man.find();

	ls_pres = []
	ls_vp = []
	ls_sec = []
	ls_treas = []
	ls_sport = []
	ls_media = []
	ls_pr = []
	ls_cul = []
	ls_yrep4 = []
	ls_yrep3 = []
	ls_yrep2 = []

	for doc in cursor:
		if doc['position'] == "President":
			ls_pres.append([doc['name'],doc['comment'],doc['manifesto'],doc['_id']])
		elif doc['position'] == "VP":
			ls_vp.append([doc['name'],doc['comment'],doc['manifesto'],doc['_id']])
		elif doc['position'] == "Secretary":
			ls_sec.append([doc['name'],doc['comment'],doc['manifesto'],doc['_id']])
		elif doc['position'] == "Treasurer":
			ls_treas.append([doc['name'],doc['comment'],doc['manifesto'],doc['_id']])
		elif doc['position'] == "Sports":
			ls_sport.append([doc['name'],doc['comment'],doc['manifesto'],doc['_id']])
		elif doc['position'] == "Media":
			ls_media.append([doc['name'],doc['comment'],doc['manifesto'],doc['_id']])
		elif doc['position'] == "PR":
			ls_pr.append([doc['name'],doc['comment'],doc['manifesto'],doc['_id']])
		elif doc['position'] == "Cultural":
			ls_cul.append([doc['name'],doc['comment'],doc['manifesto'],doc['_id']])
		elif doc['position'] == "YearRep4":
			ls_yrep4.append([doc['name'],doc['comment'],doc['manifesto'],doc['_id']])
		elif doc['position'] == "YearRep3":
			ls_yrep3.append([doc['name'],doc['comment'],doc['manifesto'],doc['_id']])
		elif doc['position'] == "YearRep2":
			ls_yrep2.append([doc['name'],doc['comment'],doc['manifesto'],doc['_id']])

	random.shuffle(ls_pres)
	random.shuffle(ls_vp)
	random.shuffle(ls_sec)
	random.shuffle(ls_treas)
	random.shuffle(ls_sport)
	random.shuffle(ls_media)
	random.shuffle(ls_pr)
	random.shuffle(ls_cul)
	random.shuffle(ls_yrep4)
	random.shuffle(ls_yrep3)
	random.shuffle(ls_yrep2)

	return template('views/index.html', ls_pres=ls_pres,
								  ls_vp=ls_vp,
								  ls_sec=ls_sec,
								  ls_treas=ls_treas,
								  ls_sport=ls_sport,
								  ls_media=ls_media,
								  ls_pr=ls_pr,
								  ls_cul=ls_cul,
								  ls_yrep4=ls_yrep4,
								  ls_yrep3=ls_yrep3,
								  ls_yrep2=ls_yrep2,
								  page="candidates")

@route("/myvote", method="GET")
@route("/myvote", method="POST")
def vote():
	get_code = request.forms.code
	get_president = request.forms.president
	get_vice_president = request.forms.vice_president
	get_secretary = request.forms.secretary
	get_treas = request.forms.treas
	get_sports = request.forms.sports
	get_media = request.forms.media
	get_pr = request.forms.pr
	get_cul = request.forms.cul
	get_yrep4 = request.forms.yrep4
	get_yrep3 = request.forms.yrep3
	get_yrep2 = request.forms.yrep2
	client = MongoClient('mongodb://admin:admin@ds031581.mongolab.com:31581/heroku_app34859325')
	db = client.get_default_database()

	man = db['man']
	votes = db['votes']
	cookies = db['cookies']

	cursor_man = man.find();

	ls_pres = []
	ls_vp = []
	ls_sec = []
	ls_treas = []
	ls_sports = []
	ls_media = []
	ls_pr = []
	ls_cul = []
	ls_yrep4 = []
	ls_yrep3 = []
	ls_yrep2 = []

	for doc in cursor_man:
		if doc['position'] == "President":
			ls_pres.append(doc['name'])
		elif doc['position'] == "VP":
			ls_vp.append(doc['name'])
		elif doc['position'] == "Secretary":
			ls_sec.append(doc['name'])
		elif doc['position'] == "Treasurer":
			ls_treas.append(doc['name'])
		elif doc['position'] == "Sports":
			ls_sports.append(doc['name'])
		elif doc['position'] == "Media":
			ls_media.append(doc['name'])
		elif doc['position'] == "PR":
			ls_pr.append(doc['name'])
		elif doc['position'] == "Cultural":
			ls_cul.append(doc['name'])
		elif doc['position'] == "YearRep4":
			ls_yrep4.append(doc['name'])
		elif doc['position'] == "YearRep3":
			ls_yrep3.append(doc['name'])
		elif doc['position'] == "YearRep2":
			ls_yrep2.append(doc['name'])

	new_cursor = votes.find()
	code_ls = []

	for doc in new_cursor:
		try:
			code_ls.append(doc['code'])
		except:
			pass

	access = True
	blank = False
	all_filled = False

	if not get_code:
		blank = True
	if get_code in code_ls and not blank:
		access = False
	if get_president and get_vice_president and get_secretary and get_treas and get_sports and get_media and get_pr and get_cul and get_yrep4 and get_yrep3 and get_yrep2:
		all_filled = True
	
	if get_code:
		if len(get_code) == 6:
			first = get_code[0]
			second = get_code[1]
			third = get_code[2]
			forth = get_code[3]
			fifth = get_code[4]
			sixth = get_code[5]

			if first not in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890':
				access = False
			if second not in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
				access = False
			if third not in '1234567890':
				access = False
			if forth not in '13579':
				access = False
			if fifth not in '2015':
				access = False
			if sixth not in 'zahir':
				access = False
		else:
			access = False

	if access and not blank and all_filled:
		votes.insert({"code":str(get_code),
					  "president":str(get_president),
					  "vice_president":str(get_vice_president),
					  "secretary":str(get_secretary),
					  "treasurer":str(get_treas),
					  "sports":str(get_sports),
					  "media":str(get_media),
					  "pr":str(get_pr),
					  "cul":str(get_cul),
					  "yrep4":str(get_yrep4),
					  "yrep3":str(get_yrep3),
					  "yrep2":str(get_yrep2)
					  })
		cookies.insert({"code":get_code, "cookie":eat_cookies()})

		client.close()
		# return template('index.html',success=True)
		return redirect()
	else:
		client.close()
		return template('views/vote.html', ls_pres=ls_pres,
									 ls_vp=ls_vp,
									 ls_sec=ls_sec,
									 ls_treas=ls_treas,
									 ls_sports=ls_sports,
									 ls_media=ls_media,
									 ls_pr=ls_pr,
									 ls_cul=ls_cul,
									 ls_yrep4=ls_yrep4,
									 ls_yrep3=ls_yrep3,
									 ls_yrep2=ls_yrep2,
									 complete=False,
									 c=get_code,
									 p=get_president,
									 vp=get_vice_president,
									 s=get_secretary,
									 treas=get_treas,
									 sports=get_sports,
									 media=get_media,
									 pr=get_pr,
									 cul=get_cul,
									 yrep4=get_yrep4,
									 yrep3=get_yrep3,
									 yrep2=get_yrep2,
									 page="vote",
									 access=access,
									 all_filled=all_filled,
									 blank=blank)

@route("/resultx")
def redirect():
	print_list = []
	president_count = {}
	vice_president_count = {}
	sec_count = {}
	treas_count = {}
	sports_count = {}
	media_count = {}
	cul_count = {}
	pr_count = {}
	yrep4_count = {}
	yrep3_count = {}
	yrep2_count = {}
	client = MongoClient('mongodb://admin:admin@ds031581.mongolab.com:31581/heroku_app34859325')
	db = client.get_default_database()
	votes = db['votes']

	cursor = votes.find();

	for doc in cursor:
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

			if doc['yrep4'] not in yrep4_count:
				yrep4_count[doc['yrep4']] = 1
			else:
				yrep4_count[doc['yrep4']] += 1

			if doc['yrep3'] not in yrep3_count:
				yrep3_count[doc['yrep3']] = 1
			else:
				yrep3_count[doc['yrep3']] += 1

			if doc['yrep2'] not in yrep2_count:
				yrep2_count[doc['yrep2']] = 1
			else:
				yrep2_count[doc['yrep2']] += 1
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
	pr = []
	yrep4 = []
	yrep3 = []
	yrep2 = []

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
	for key in yrep4_count:
		yrep4.append([key, yrep4_count[key]])
	for key in yrep3_count:
		yrep3.append([key, yrep3_count[key]])
	for key in yrep2_count:
		yrep2.append([key, yrep2_count[key]])

	# pc.sort(key=lambda tup: tup[1], reverse=True)
	# vpc.sort(key=lambda tup: tup[1], reverse=True)
	# sc.sort(key=lambda tup: tup[1], reverse=True)
	# treas.sort(key=lambda tup: tup[1], reverse=True)
	# sports.sort(key=lambda tup: tup[1], reverse=True)
	# media.sort(key=lambda tup: tup[1], reverse=True)
	# cul.sort(key=lambda tup: tup[1], reverse=True)
	# pr.sort(key=lambda tup: tup[1], reverse=True)
	# yrep4.sort(key=lambda tup: tup[1], reverse=True)
	# yrep3.sort(key=lambda tup: tup[1], reverse=True)
	# yrep2.sort(key=lambda tup: tup[1], reverse=True)

	client.close()
	return template('views/result.html', pc=pc,
								   vpc=vpc,
								   sc=sc,
								   treas=treas,
								   sports=sports,
								   media=media,
								   cul=cul,
								   pr=pr,
								   yrep4=yrep4,
								   yrep3=yrep3,
								   yrep2=yrep2,
								   page="result")

from bson.objectid import ObjectId

@route("/manifesto", method="GET")
@route("/manifesto", method="POST")
def manifesto():
	client = MongoClient('mongodb://admin:admin@ds031581.mongolab.com:31581/heroku_app34859325')
	db = client.get_default_database()
	man = db['man']
	ls = []

	get_id = str(request.forms.man_id)
	get_sid = get_id[1:25]
	fb_id = get_id[25:]

	logging_err = False

	existing_voter = False

	if get_sid:
		upvotes = db['upvotes']
		up_cursor = upvotes.find({'username':fb_id})
		for doc in up_cursor:
			if doc['vote_id'] == get_id[:25]:
				existing_voter = True

		if not existing_voter and fb_id:
			upvotes.insert({"username":fb_id,
							"vote_id":get_id[:25],
							"cookie":eat_cookies(),
							"browser":browser_info()})
			get_index = int(get_id[:1])
			new_c = man.find({"_id":ObjectId(get_sid)})

			for doc in new_c:
				doc['manifesto'][get_index][1] += 1
			man.update({'_id':doc['_id']}, {"$set":doc})

		if not fb_id:
			logging_err = True

	cursor = man.find()

	rank_ls = []
	man_score = 0
	for doc in cursor:
		manifest = doc['manifesto']
		for i in manifest:
			if i[0] not in ['1','2','3']:
				i.append(doc['position'])
				i.append(doc['name'])
				ls.append(i)
			man_score += i[1]
		rank_ls.append([doc['name'], doc['position'], man_score])
		man_score = 0

	# for rank in rank_ls:
	# 	print rank

	pos_ls = man.distinct("position")

	high_rank_dict = {}
	prev = 0
	for pos in pos_ls:
		for rank in rank_ls:
			if pos == rank[1]:
				if rank[2] > prev:
					high_rank_dict[pos] = [rank[0], rank[2]]
					prev = rank[2]
		prev = 0

	r = []
	for key in high_rank_dict:
		if key == 'President':
			r.append([key, high_rank_dict[key][0], high_rank_dict[key][1], 0])
		elif key == 'VP':
			r.append(['Vice President', high_rank_dict[key][0], high_rank_dict[key][1], 1])
		elif key == 'Secretary':
			r.append([key, high_rank_dict[key][0], high_rank_dict[key][1], 2])
		elif key == 'Treasurer':
			r.append([key, high_rank_dict[key][0], high_rank_dict[key][1], 3])
		elif key == 'Sports':
			r.append(['Sports Officer', high_rank_dict[key][0], high_rank_dict[key][1], 4])
		elif key == 'Media':
			r.append(['Media Officer', high_rank_dict[key][0], high_rank_dict[key][1], 5])
		elif key == 'PR':
			r.append(['PR Officer', high_rank_dict[key][0], high_rank_dict[key][1], 6])
		elif key == 'Cultural':
			r.append(['Cultural Affair Officer', high_rank_dict[key][0], high_rank_dict[key][1], 7])
		elif key == 'YearRep4':
			r.append(['4th Year Rep.', high_rank_dict[key][0], high_rank_dict[key][1], 8])
		elif key == 'YearRep3':
			r.append(['3rd Year Rep.', high_rank_dict[key][0], high_rank_dict[key][1], 9])
		elif key == 'YearRep2':
			r.append(['2nd Year Rep.', high_rank_dict[key][0], high_rank_dict[key][1], 10])

	ls.sort(key=lambda tup: tup[1], reverse=True)
	r.sort(key=lambda tup:tup[3], reverse=False)

	# Code to add manifesto infographics

	client.close()
	return template('views/manifesto.html', page="manifesto",
											ls=ls,
											logging_err=logging_err,
											r=r)

from collections import Counter
@route("/ask", method="GET")
@route("/ask", method="POST")
def ask():
	client = MongoClient('mongodb://admin:admin@ds031581.mongolab.com:31581/heroku_app34859325')
	db = client.get_default_database()
	man = db['man']
	ask = db['ask']
	candidate_ls = man.distinct("name")
	candidate_ls.sort(key=lambda tup: tup[0], reverse=False)

	question_ls = []

	get_candidate = request.forms.candidates
	get_question= request.forms.question
	get_id = str(request.forms.qid)
	get_qid = get_id[:24]
	fb_id = get_id[24:]

	blank = False
	if not get_question or not get_candidate:
		blank=True

	access = False
	cmp_fb_id = ''
	if get_qid:
		ask_cursor_2 = ask.find({'_id':ObjectId(get_qid)})
		for doc in ask_cursor_2:
			cmp_fb_id = doc['fb']
		if cmp_fb_id == fb_id:
			access = ObjectId(get_qid)

	# has_cookie = cookies.find({'candidate':cookie}).count()

	if not blank:
		get_fb_asker = request.forms.fb_asker

		man_cursor = man.find({'name':get_candidate})
		insert_fb = ''
		for doc in man_cursor:
			insert_fb = doc['fb']
		ask.insert({"candidate":str(get_candidate),
					 "question":str(get_question),
					 "cookie":eat_cookies(),
					 "fb":insert_fb,
					 "fb_asker":get_fb_asker,
					 "date":est_time(),
					 "score":0,
					 "likes":[],
					 "browser_info":browser_info()
					  })

	get_answer = request.forms.answer
	get_aid = request.forms.aid
	if get_answer:
		ask_cursor_3 = ask.find({'_id':ObjectId(get_aid)})
		for doc in ask_cursor_3:
			doc['answer'] = get_answer
			doc['date'] = est_time()
			ask.update({'_id':doc['_id']}, {"$set":doc})

	get_filter = request.query.filter
	get_u = request.query.u

	# Implementing Voting System for Q and A
	get_vvid = str(request.forms.vid)
	get_vid = get_vvid[1:25]
	v_fb_id = get_vvid[25:]

	logging_err = False

	existing_voter = False

	if get_vid:
		v_ask_cursor = ask.find({'_id':ObjectId(get_vid)})

		for doc in v_ask_cursor:
			if v_fb_id in doc['likes']:
				existing_voter = True

		if not existing_voter and v_fb_id:
			ve_ask_cursor = ask.find({'_id':ObjectId(get_vid)})

			for doc in ve_ask_cursor:
				temp = doc['likes']
				temp.append(v_fb_id)
				temp_score = len(temp)
				doc['likes'] = temp
				doc['score'] = temp_score

			ask.update({'_id':ObjectId(get_vid)}, {"$set":doc})

		if not v_fb_id:
			logging_err = True

	ask_cursor = ask.find()

	answer = ''
	answered = 0
	for doc in ask_cursor:
		try:
			answer = doc['answer']
			if answer:
				answered = 1
		except:
			pass
		question_ls.append([doc['candidate'], doc['question'], answer, doc['_id'], doc['date'], answered, doc['score']])
		answer = ''
		answered = 0

	question_ls.sort(key=lambda tup: tup[5], reverse=True)
	question_ls.sort(key=lambda tup: tup[6], reverse=True)

	if get_filter == "candidate":
		question_ls.sort(key=lambda tup: tup[0], reverse=False)
	elif get_filter == "answered":
		question_ls.sort(key=lambda tup: tup[0], reverse=False)
		question_ls.sort(key=lambda tup: tup[5], reverse=True)
	elif get_filter == "unanswered":
		question_ls.sort(key=lambda tup: tup[0], reverse=False)
		question_ls.sort(key=lambda tup: tup[5], reverse=False)

	dates = ask.distinct("date")
	new_q_ls = []
	temp = []
	for d in dates:
		for q in question_ls:
			if d == q[4]:
				temp.append(q)
		new_q_ls.append([d,temp])
		temp = []

	new_q_ls.sort(key=lambda tup: tup[0], reverse=True)

	# get candidate names and questions asked
	q_asked = []
	q_name = [i[0] for i in question_ls]

	man_for_q = []
	c = Counter(q_name)
	for i in candidate_ls:
		man_cursor_2 = man.find({'name':i})
		for doc in man_cursor_2:
			for e in doc['manifesto']:
				if e[0] not in ['1','2','3']:
					man_for_q.append(e[0])
		str_q = ', '.join(man_for_q)
		q_asked.append([i, c[i], str_q])
		man_for_q = []

	q_asked.sort(key=lambda tup: tup[1], reverse=False)

	client.close()
	return template('views/ask.html', page="ask",
									  candidate_ls=candidate_ls,
									  question_ls=question_ls,
									  access=access,
									  new_q_ls=new_q_ls,
									  u=get_u,
									  q_asked=q_asked)

@route("/admin", method="GET")
@route("/admin", method="POST")
def admin():
	client = MongoClient('mongodb://admin:admin@ds031581.mongolab.com:31581/heroku_app34859325')
	db = client.get_default_database()
	man = db['man']
	ask = db['ask']
	removed = db['removed']
	candidate_ls = man.distinct("name")

	question_ls = []

	get_candidate = request.forms.candidates
	get_question= request.forms.question
	get_id = str(request.forms.qid)
	get_qid = get_id[:24]
	fb_id = get_id[24:]

	blank = False
	if not get_question or not get_candidate:
		blank=True

	access = False
	admin_id = ['Mohd Fathuddin Romeli','Anas Faris','Ahmad Zahir Shaifuddin','Muzakkir Mohamad']
	doc_to_del = False
	if get_qid:
		if fb_id in admin_id:
			ask_cursor_del = ask.find({'_id':ObjectId(get_qid)})
			for doc in ask_cursor_del:
				answer = ''
				try:
					answer = doc['answer']
				except:
					pass
				removed.insert({"candidate":doc['candidate'],
							 "question":doc['question'],
							 "cookie":eat_cookies(),
							 "answer":answer,
							 "deleter_fb":fb_id,
							 "date":est_time()
							  })
				answer = ''
			db.ask.remove({'_id':ObjectId(get_qid)})

	get_answer = request.forms.answer
	get_aid = request.forms.aid
	if get_answer:
		ask_cursor_3 = ask.find({'_id':ObjectId(get_aid)})
		for doc in ask_cursor_3:
			doc['answer'] = get_answer
			ask.update({'_id':doc['_id']}, {"$set":doc})

	ask_cursor = ask.find()

	answer = ''
	for doc in ask_cursor:
		try:
			answer = doc['answer']
		except:
			pass
		question_ls.append([doc['candidate'], doc['question'], answer, doc['_id']])
		answer = ''

	client.close()
	return template('views/admin.html', page="ask",
									  candidate_ls=candidate_ls,
									  question_ls=question_ls,
									  access=access)

run(reloader=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8000)))
