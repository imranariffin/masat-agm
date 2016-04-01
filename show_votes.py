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

