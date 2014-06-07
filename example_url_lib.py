import urllib2


from bluesmen import bluesmen

for bluesman in bluesmen:
    response = urllib2.urlopen('http://en.wikipedia.org/w/api.php?format=json&action=query&titles='+bluesman+'&prop=revisions&rvprop=content')
    html = response.read()

    with open( bluesman+'.json', 'w') as f:
        f.write( "Get all data: ", html)
