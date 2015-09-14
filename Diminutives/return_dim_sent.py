""" For those times when you want all of the nouns in you sentence to be transformed to their diminutive forms.
Using CLiPS pattern.nl to parse the sentences to find nouns and turning plural nouns into their singular form.

Uses the Diminutive-generator to turn nouns into their diminutive form.
"""

from pattern.nl import parse, singularize
import diminutive_generator as dg


def return_dim_sent(sent):
	""" Takes in a string sentence and checks if there are nouns in that sentence. If there are, it 
	returns the sentence with the noun in their diminutive form.

	:param sent: a string containing a sentence. 
	:return: a string containging the sentence with the nouns turned to diminutives.
	:rtype: str
	"""

	parsed = parse(sent, tokenize = True, tags = True, chunks = False)

	new_sent = []
	for word, pos in parsed.split()[0]:
	    if pos == 'NN' and not word.endswith('je'):    # If the word is a noun...
	        dim = dg.generate_diminutive(word)
	        new_sent.append(dim)
	    elif pos == 'NNS' and not word.endswith('jes'): # If the word is a noun in plural...
	        root = singularize(word)
	        dim = dg.generate_diminutive(root)
	        new_sent.append(dim + "s")
	    else:
	        new_sent.append(word)
    
    

	return " ".join(new_sent)





if __name__ == "__main__":
	sent = "De katten liggen in de zon."
	sent1 = "De mussen zitten op het dak."

	print return_dim_sent(sent)
	print return_dim_sent(sent1)

