#Vers 1
def next_item(xs, item):
	try:
		xs = iter(xs)
		while next(xs) != item: pass
		return next(xs)
	except:
		return None


#Vers 2
def next_item(xs, item):
	try:
		xs = iter(xs)
		while next(xs) != item: pass
		return next(xs)
	except:
			return None