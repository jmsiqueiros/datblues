import urllib2


from bluesmen import bluesmen

for bluesman in bluesmen:
    response = urllib2.urlopen('http://en.wikipedia.org/w/api.php?format=json&action=query&titles='+bluesman+'&prop=revisions&rvprop=content')
    html = response.read()

    print "bajando %s" % bluesman
    with open( bluesman+'.json', 'w') as f:
        f.write( html)
