#Vers 1
def geometric_sequence_elements(a, r, n):
	return ', '.join([str(a * r ** i) for i in range(n)])

#Vers 2
def geometric_sequence_elements(a, r, n):
	list_result = [a * r**i for i in range(n)]
	str_result = ", ".join([str(i) for i in list_result])

	return str_result