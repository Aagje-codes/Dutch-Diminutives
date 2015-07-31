""" 
De or het?
One of the harderst things for Dutch language learners to get a grip on, 
is the article of a noun. 
Dutch makes use of two definite articles: 'de' (masculine and femenine) and 
'het' (neuter) of which 'de' is the most common.
To a learner it may seem arbitrary when to use which (it certainly feels that way even to
native Dutch speakers), however, there are a few rules that determine when to use 
which article.

These rules include, but are not limited to:
* for 'de':
	- the plural form;
	- numbers and ordinals ('de een, de eerste')
	- rivers ('de Maas')
	- fruit & vegetables ('de appel', 'de broccoli')
	- 

* for 'het':
	- diminutives (singular form only)
	- games & sports ('het basketbal')
	- colors ('het blauw van je ogen')
	- langauges ('het spaans', 'het nederlands')
	- metals

And then of course there are plenty of exceptions.


So, let's build something around this. 

This is an article checker that takes in a noun and returns it with 
the correct article.
"""



def de_or_het(noun):
	# take in a noun, return the noun with a correct article.
	article = []

	# we have an excel file with 'het'-words that I've been building since forever
	with open('het_woorden.csv', 'r') as csv:
		het_woorden = csv.read()
		

	return article, noun


if __name__ == '__main__':
	lijstje = ['man', 'vrouw', 'jongen', 'meisje']

	for word in lijstje:
		print de_or_het(word)