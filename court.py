from xml.etree import ElementTree

with open('D:/abc.xml', 'rt') as f:
    tree = ElementTree.parse(f)
count = 0
crime_names = ['murder','kidnapping','robbery']
for node in tree.iter():
    if node.tag in crime_names:
        print "Crime Name: ", node.tag
    else:
        if node.attrib:
            print "\t" , node.tag, ": ", node.attrib['value']
        else: 
            print node.tag
    