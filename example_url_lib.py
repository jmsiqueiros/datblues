import urllib2


artista = "Chris_Martin"
response = urllib2.urlopen('http://en.wikipedia.org/w/api.php?format=json&action=query&titles='+artista+'&prop=revisions&rvprop=content')
html = response.read()
print "Get all data: ", html
