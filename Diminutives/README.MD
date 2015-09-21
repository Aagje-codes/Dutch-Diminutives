This is an attempt to create a Dutch Diminutives Generator for Python 2.7

The **generate_diminutive** function takes in a noun and returns the diminutive form. 

The __return_dim_sent__ function takes in a Dutch sentence and uses the CLiPS Pattern module for Dutch to find the 
nouns (singular or plural) and return the sentence with the nouns replaced as their diminutives. 
Corrects for articles when the article is directly precedeing the noun, but not otherwise. 

***

Tests: 
+ generate_diminutive('boek') -> boekje
+ generate_diminutive('tafel') -> tafeltje
+ generate_diminutive('bel') -> belletje

+ return_dim_sent("De premier wil de kroon.") -> De premier wil het kroontje .
+ return_dim_sent("De mussen ziten op het dak") -> De musjes zitten op het dakje .
+ return_dim_sent("De katten liggen in de zon") -> De katjes liggen in het zonnetje .