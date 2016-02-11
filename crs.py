from xml.etree.ElementTree import Element, SubElement, Comment, tostring
from xml.etree import ElementTree
from xml.dom import minidom
import os

def prettify(elem):
    """Return a pretty-printed XML string for the Element.
    """
    rough_string = ElementTree.tostring(elem, 'utf-8')
    reparsed = minidom.parseString(rough_string)
    return reparsed.toprettyxml(indent="  ")
def getsummary (root):
    summary = SubElement(root, 'summary')
    date =  raw_input("Enter crime date: ");
    SubElement(summary, 'date',{'value':date})
    location= raw_input("Enter crime location: ");
    SubElement(summary, 'location',{'value':location})
def getvictim (root):
    victim = SubElement(root, 'victim')
    name= raw_input("Enter victim name: ")
    SubElement(victim, 'name', {'value':name})
    address = raw_input("Enter victim address: ");
    SubElement(victim, 'address',{'value':address})
    age= raw_input("Enter victim age: ");
    SubElement(victim, 'age',{'value':age})
    occupation = raw_input("Enter victim occupation: ")
    SubElement(victim, 'occupation',{'value':occupation})
    cell_number = raw_input("Enter victim cell number: ");
    SubElement(victim, 'cell_number',{'value':cell_number})
    sex = raw_input("Enter victim sex: ");
    SubElement(victim, 'sex',{'value':sex})
def getwitness(root):
    no_of_witnessess = int(raw_input("Enter number of witnessess: "));
    witnesses = SubElement(root, 'witnesses')
    for i in range(0,no_of_witnessess):
        witness = SubElement(witnesses, 'witness')    
	name = raw_input("Enter witness name: ");
	SubElement(witness, 'name',{'value': name})
	address= raw_input("Enter witness address: ")
	SubElement(witness, 'address',{'value':address})
	age= raw_input("Enter witness age: ");
        SubElement(witness, 'age',{'value':age})
	occupation= raw_input("Enter witness occupation: ")
	SubElement(witness, 'occupation',{'value',occupation})
	cell_number = raw_input("Enter witness cell number: ");
	SubElement(witness, 'cell_number',{'value':cell_number})
	sex = raw_input("Enter witness sex: ");
	SubElement(witness, 'sex',{'value':sex})
	relationship = raw_input("Enter witness relationship with victim: ");
	SubElement(witness, 'relationship',{'value':relationship})
def getstolenitems (root):
    stolen_items = SubElement(root, 'stolen_items')
    no_of_stolen_items = int( raw_input("How many item has stolen? "))
    for i in range(0,no_of_stolen_items):
        items = SubElement(stolen_items, 'items')
    	name = raw_input("Enter item name: ")
    	SubElement(items, 'name',{'value':name})
    	price = raw_input("Enter item price: ")
    	SubElement(items, 'price',{'value':price})
    	color = raw_input("Enter item color: ")
    	SubElement(items, 'color',{'value':color})
    	company_name = raw_input("Enter item company name: ")
    	SubElement(items, 'company_name',{'value':company_name})
    	quantity= raw_input("Enter item quantity: ")
    	SubElement(items, 'quantity',{'value': quantity})
    	
def getevidences(root):
    evidences = SubElement(root, 'evidences')
    no_of_evidences = int(raw_input("Enter number of evidences collected"))
    for i in range(0,no_of_evidences):
        evidence = raw_input("Enter the name of evidance: ")
        SubElement(evidences, 'evidence',{'value':evidence})
    
def gettoolused(root):
    tool_used = SubElement(root, 'tool_used')
    tool = int (raw_input("Select tool uses in murder. 1-Gun 2-Knife 3-Posion"))
    if tool==1:
       Gun = SubElement(tool_used, 'Gun')
       gun_model= raw_input("Enter Gun model")
       SubElement(Gun, 'gun_model',{'value':gun_model}) 
    elif tool==2:
       knife = SubElement(tool_used, 'knife')
       manufacturer_name = raw_input("Enter knife manufacturer name")
       SubElement(knife, 'manufacturer_name',{'value':manufacturer_name})
    elif tool==3:
       poision = SubElement(tool_used, 'posion')
       name= raw_input("Enter poison name")
       SubElement(poision,'name',{'value':name})
    else:
        print ("Wrong option selected")

def getkidnappers(root):
    kidnappers = SubElement(root, 'kidnappers')
    no_of_kidnappers= int (raw_input("Enter number of kidnappers"))
    SubElement(kidnappers, 'no_of_kidnappers',{'value':no_of_kidnappers})
    mode_of_carry = (raw_input("Enter mode used to carry victim"))
    SubElement(kidnappers, 'mode_of_carry',{'value':mode_of_carry})                	    	               	       
print ("Welcome to Crime Reporting System")
crs = open('D:/pythonxml/crs.xml', 'w')
option=0
crime = Element('crime')
while option!=4:
	print ("Please select a crime to report")
	print (" 1- Robbery")	
	print (" 2- Murder")
	print (" 3- Kidnapping")
	print (" 4- Exit")
	option = input("Enter your choice: ");
	if option==1:
	       robbery = Element('robbery')
	       robbery = SubElement(crime, 'robbery')
	       getsummary(robbery)
	   
               'victim'
	       getvictim(robbery)
	       
	       'witness'
	       getwitness(robbery)
	           
    	       
    	       'Stolen Items'
    	       getstolenitems(robbery)
    	       
    	       'evidences'
    	       getevidences(robbery)
    	       print tostring(robbery)
	       xml= prettify(robbery)
               crs.write(xml)     
    	if option==2:
    	
    	    murder = SubElement(crime, 'murder')
	    getsummary(murder)
	   
            'victim'
	    getvictim(murder)
	       
	    'witness'
	    getwitness(murder)
	    
	    'tool used'
	    gettoolused(murder)
	           
    	    'evidences'
    	    getevidences(murder)
	    xml = prettify(murder)
	    crs.write(xml)
        if option==3:
            kidnapping = SubElement(crime, 'kidnapping')
	    getsummary(kidnapping)
	   
            'victim'
	    getvictim(kidnapping)
	       
	    'witness'
	    getwitness(kidnapping)
	    
	    'kidnappers'
	    getkidnappers(kidnapping)
	           
    	    'evidences'
    	    getevidences(kidnapping)
    	    xml= prettify(kidnapping)
            crs.write(xml)    
crs.close()    	 
	
