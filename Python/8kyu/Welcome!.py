#Vers 1
db = {
'english': 'Welcome',
'czech': 'Vitejte',
'danish': 'Velkomst',
'dutch': 'Welkom',
'estonian': 'Tere tulemast',
'finnish': 'Tervetuloa',
'flemish': 'Welgekomen',
'french': 'Bienvenue',
'german': 'Willkommen',
'irish': 'Failte',
'italian': 'Benvenuto',
'latvian': 'Gaidits',
'lithuanian': 'Laukiamas',
'polish': 'Witamy',
'spanish': 'Bienvenido',
'swedish': 'Valkommen',
'welsh': 'Croeso'}

def greet(language):
    return db.get(language, "Welcome")


#Vers2
def greet(language):

	variants = {
		'english': 'Welcome',
		'czech': 'Vitejte',
		'danish': 'Velkomst',
		'dutch': 'Welkom',
		'estonian': 'Tere tulemast',
		'finnish': 'Tervetuloa',
		'flemish': 'Welgekomen',
		'french': 'Bienvenue',
		'german': 'Willkommen',
		'irish': 'Failte',
		'italian': 'Benvenuto',
		'latvian': 'Gaidits',
		'lithuanian': 'Laukiamas',
		'polish': 'Witamy',
		'spanish': 'Bienvenido',
		'swedish': 'Valkommen',
		'welsh': 'Croeso'
	}

	return variants[language] if language in variants.keys() else variants['english']