import string

unlisterized = """
1. Introduce MASWin4all (pronounce: MASWin) - abbreviated from MASAT Fall/Winter Sports - as an upgraded version of previous MASWin. Now, all MASAT members can participate actively in sports not only during Winter. Let's stay healthy and active! #MASWin4all

2. Promote and organise a wide variety of sports and games; current sports (futsal, badminton, basketball, bowling etc), traditional games (congkak etc), board games, eSports (Dota 2, FIFA etc), and extreme sports (EdgeWalk at CN Tower, skydiving etc), to bridge the gap among all MASAT members. #SukanAlatPerpaduan

3. Aiming to maintain or improve physical ability and skills while providing enjoyment to participants, and also entertainment for the spectators through the sport events that will be held. #FitFam
"""

# def listerize(string):
# 	ret = []
# 	for char in string:
# 		if char 

BIG_NUM = 99
def is_int(string):
	num_list = [str(n) for n in range(BIG_NUM)]
	if string in num_list:
		return True
	else:
		return False

def is_num_bullet(string, i):
	j = i
	while is_int(string[j]):
		j += 1
	if string[j]=="."  and j!=i:
		return True
	return False

def listerize(string):
	i = 0
	ret = []
	count = 0
	for j in range(len(string)):
		if is_num_bullet(string, j):		
			if count!=0:
				ret.append(str(count) + string[i:j])
			else:
				ret.append(string[i:j])
			i = j+1
			count += 1
		if j==len(string)-1:
			if count!=0:
				ret.append(str(count) + string[i:len(string)])
			else:
				ret.append(string[i:len(string)])
	return ret

def remove_right_space(string):
	ret = string.split(" ")
	while True:
		try:
			ret.remove("")
		except:
			break
	return ret

def paragraphize(string):
	listerized = listerize(string)
	return map(lambda e: "<p>" + e + "</p>", listerized)

if __name__=="__main__":

	print listerize("list 1.code 2.sleep ... 3.code")
	for item in listerize(unlisterized):
		print item
	
	print(listerize(unlisterized))

	# print remove_right_space(listerize(unlisterized))
	# print paragraphize(remove_right_space(listerize(unlisterized)))