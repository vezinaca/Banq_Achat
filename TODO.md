
project A: scrape BANQ search results

high level overview:
- use 'requests' library
- get the url, but change the user-agent... (actually, might not be
necessary...! try)
- use 'beautifulsoup' (bs4) library to parse the html page
- find the actual search results (the "Catalogue" results) in the html
page using beautifulsoup


# DISCUSSION ENTRE GREG ET CARL
# CARL - I am aware of the hard coded stuff in there.
# GREG - Well, if you are aware of it, why are you keeping it in there?

#Would it be better if this function had a 'return'? i.e elementsTrouves = scrapeCatalogue()
#Then I would iterate and print the elementsTrouves array?

'''
I'm able to get all the <a> tags that are in '#RMS_afficherIris .ValorisationListeDesc a'. 
However as you can see, they are not all titles.  One of them in this case is a 
link to 'Acces par PRETNUMERIQUE.CA (format ePub)', which I don't want.  I guess it doesn't 
really matter, seeing as obviously this will never be a match with what I'm looking for.  I still
think it's better to get rid of it. 

To do so, I think I would need to 'extract' the <span class="pRchrContent"> from the document then go get
the <a> tags the same way I'm proceeding now.

I've tried a couple of things I saw in the documentation, but It doesn't seem to work.  

'''



