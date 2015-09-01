# Diminutive generator for Dutch
# For Python 2.7

# Dutch is a language that uses a diminutive form of their nouns. So, for example: 'a table' is a ' een tafel' 
# in Dutch, but 'a small table' becomes 'een tafeltje'. In Dutch it isn't always clear what article 
# the noun takes, the feminin/masculine 'de' or the neutral 'het'. The Dutch diminutives are 
# useful here, because nouns in the diminutive form always take on the neutral article 'het'
# (unless the noun takes on the plural diminutive form by adding 's' after 'je', then
# the noun will take on the feminin/masculin article 'de'.) 

# This little program takes in the singular form of a noun and returns its diminutive.
# It takes exceptions into consideration, but it is plausible that other exceptions to these rules have been overlooked.

#The Dutch diminutives use the following suffices: 

# -je
# -tje
# -pje
# -etje
# -consonant+etje
# -long_vowel+tje
# exceptions

# Source for examples, see also: Syllables in Dutch - Mieke Trommelen
# and Dutch plural rules on Dutchgrammar.com



long_vowels = "aa", "ee", "ie", "oo", "uu"
short_vowels = 'a', 'e', 'i', 'o', 'u'
combination_vowels = 'au', 'ou', 'ui', 'oe', 'ei', 'ij', 'eu', 'y', 'aai', 'oei', 'ooi'
vowels = long_vowels + short_vowels + combination_vowels
common_consonants = 'b', 'c', 'd', 'f', 'ch', 'k', 'p', 'q', 's', 't', 'x', 'z'
uncommon_consonants = 'h', 'j' 'v' #Uncommon word endings in Dutch
consonants = common_consonants + uncommon_consonants
soft_endings = 'n', 'l', 'r', 'w', 'm', 'g'
	

def etje(noun):
	return noun + 'etje'	
	
def C_etje(noun):
	return noun + noun[-1] + 'etje'

def pje(noun):
	return noun + 'pje'
	
def tje(noun):
	return noun +'tje'

def je(noun):
	return noun + 'je'

 					
def check_for_softendings(noun):
	# takes is a noun and checks if it satisfies the requirement. returns True or False such that 
	#the diminutive generator can take of
	# meeting the requirements means that the word_ending contains a short_vowel and ends with a soft_ending.
	# Or in our case, it means that follow regular track ('tje') if:
	# 1. long_vowels in noun[-3:] (if there are none: p1 = False)	
	# 2. combination_vowels in noun[-3:] (if there are none, p2 = False)
	# 3. noun == exceptions (if it is, return False)
	with open('diminutive_exceptions', 'r') as d:
		de = d.read()
	de = de.split('\n')
	de = [w for w in de if w] #This should get rid of empty new lines (they conflict with p3)
	
	p1 = True
	p2 = True
	p3 = True
		
	for lv in long_vowels:
		if lv in noun[-3:]:
			p1 = False
			
	for cv in combination_vowels:
		if cv in noun[-3:]:
			p2 = False		
			
	#These 'exceptions' all have in common that the word stress does not fall on the last syllable and therefore should get the word
	# ending -tje. I have not found a way to check for word stress, as it would require to chop words into syllables first and that's
	# a whole new story. For now, I've made a list of common exception, but know that this list is incomplete. 
	for w in de:
		if w == noun or noun.endswith(w):
			p3 = False
									
	en = p1 and p2 and p3
	return en

	
def vowel_ending(noun):
#	if ending in long vowels or combination vowels: False (normal route of 'tje')
# 	if ending in short vowels: then return True (exception of elongating short vowel and adding 'tje')
#	Three premises:
#	1. Noun ends in long vowel - return True and resume normal 'tje'- route
#	2. Noun ends with combination vowel - return True and resume normal 'tje'-route
#	Else: it presumably ends in Short vowel and return False.
# if 1 or 2 is true, then return true, otherwise return false
	
	p1 = False
	p2 = False
	
	#Premise 1:
	for lv in long_vowels:
		if noun.endswith(lv):
			p1 = True
	
	for cv in combination_vowels:
		if noun.endswith(cv):
			p2 = True
	
	if p1 or p2:
		return True
	else:
		return False	


def ing(noun):
	p1 = False

	exceptions = [
	'ketting', 'haring', 'koning', 'houding', 'mededeling', 'woning', 'training', 'verwarming'
	]
	for w in exceptions:
		if w == noun:
			p1 = True
		
	return p1


def general_exceptions(noun):
# Takes in a noun and returns True if the noun is an exception
	p1 = False
	
	exceptions= ['blad', 'gat', 'glas', 'lot', 'pad', 'schip', 'vat', 'lade', 'groente']
	for w in exceptions:
		if noun == w or noun.endswith(w):
			p1 = True
			
	return p1
			

	
def diminutive_generator(noun):

	assert isinstance(noun, basestring), "Argument to diminutive_generator() should be a string."

	# ends with a vowel
	if noun[-1] in vowels or noun.endswith('ij'):
		if vowel_ending(noun):
			noun = tje(noun)
		elif not general_exceptions(noun):
			if noun[-1] == 'i':
				noun = noun + 'e'
				noun = tje(noun) 	
			elif noun == 'tante':
				noun = tje(noun)
			else:
				noun = noun + noun[-1]
				noun = tje(noun)						

	# endswith -ing:
	if noun.endswith('ng'):
		if ing(noun):
			noun = je((noun[:-1]+'k'))
		else:
			noun = etje(noun)
			
	
	#returns words ending in 'n', 'l' 'r', 'm' with a short vowel in the final syllable with the correct -etje ending
	if noun.endswith(soft_endings):
		if check_for_softendings(noun):
			noun = C_etje(noun)
		elif noun.endswith('m'):
			noun = pje(noun)
		elif noun.endswith('g'):
			noun = je(noun)	
		else:	
			noun = tje(noun)
			 
	#general exceptions
	if general_exceptions(noun):
		at_words = 'vat', 'gat'
		ad_words = 'blad', 'pad'
		if noun == 'lade':
			noun = tje(noun[:-2]+'a')
		elif noun == 'kip':
			noun = C_etje(noun)		
		elif noun == 'groente':
			noun = je(noun[:-1])+'s'	
		elif noun == 'glas':
			noun = je(noun[:-1]+'as')
		elif noun == 'schip':
			noun = je(noun[:-2]+'eep')	
		elif noun == 'lot':
			noun = je(noun[:-1]+'ot')
		elif noun.endswith(at_words):	
			noun = je(noun[:-1]+'at')
		elif noun.endswith(ad_words):
			noun = je(noun[:-1]+'ad')
	
	#regular diminutive rule
	elif noun.endswith(common_consonants):
		noun = je(noun)
		
	elif noun.endswith(uncommon_consonants):
		print "This word has an uncommon word ending for Dutch and clear rules for conjugation have not been established"	

		
	return noun


if __name__ == "__main__":
	print "\nThe diminutive form of 'tafel' is:"
	print diminutive_generator('tafel')	
	print "\nThe diminutive form of 'bel' is:"
	print diminutive_generator('bel')
	print "\nThe diminutive form of 'koek' is:"
	print diminutive_generator('koek')
	print "\nThe diminutive form of 'boom' is:"
	print diminutive_generator('boom')

