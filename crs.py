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
    date = SubElement(summary, 'date')
    date.text =  raw_input("Enter crime date: ");
    location = SubElement(summary, 'location')
    location.text= raw_input("Enter crime location: ");
def getvictim (root):
    victim = SubElement(root, 'victim')
    name = SubElement(victim, 'name')
    name.text = raw_input("Enter victim name: ")
    address = SubElement(victim, 'address')
    address.text = raw_input("Enter victim address: ");
    age = SubElement(victim, 'age')
    age.text = raw_input("Enter victim age: ");
    occupation = SubElement(victim, 'occupation')
    occupation.text = raw_input("Enter victim occupation: ")
    cell_number = SubElement(victim, 'cell_number')
    cell_number.text = raw_input("Enter victim cell number: ");
    sex = SubElement(victim, 'sex')
    sex.text = raw_input("Enter victim sex: ");
def getwitness(root):
    no_of_witnessess = int(raw_input("Enter number of witnessess: "));
    witnesses = SubElement(root, 'witnesses')
    for i in range(0,no_of_witnessess):
        witness = []
	name = SubElement(witnesses, 'name')
	name.text = raw_input("Enter witness name: ");
	address = SubElement(witnesses, 'address')
	address.text = raw_input("Enter witness address: ")
	age = SubElement(witnesses, 'age')
	age.text= raw_input("Enter witness age: ");
	occupation = SubElement(witnesses, 'occupation')
	occupation.text = raw_input("Enter witness occupation: ")
	cell_number = SubElement(witnesses, 'cell_number')
	cell_number.text = raw_input("Enter witness cell number: ");
	sex = SubElement(witnesses, 'sex')
	sex.text = raw_input("Enter witness sex: ");
	relationship = SubElement(witnesses, 'relationship')
	relationship.text = raw_input("Enter witness relationship with victim: ");
def getstolenitems (root):
    stolen_items = SubElement(root, 'stolen_items')
    no_of_stolen_items = int( raw_input("How many item has stolen? "))
    for i in range(0,no_of_stolen_items):
        items = SubElement(stolen_items, 'items')
    	name = SubElement(items, 'name')
    	name.text = raw_input("Enter item name: ")
    	price = SubElement(items, 'price')
    	price.text = raw_input("Enter item price: ")
    	color = SubElement(items, 'color')
    	color.text = raw_input("Enter item color: ")
    	company_name = SubElement(items, 'company_name')
    	company_name.text = raw_input("Enter item company name: ")
    	quantity = SubElement(items, 'quantity')
    	quantity.text = raw_input("Enter item quantity: ")
    	#stolen_items.append(items)
def getevidences(root):
    evidences = SubElement(root, 'evidences')
    no_of_evidences = int(raw_input("Enter number of evidences collected"))
    for i in range(0,no_of_evidences):
        evidence = SubElement(evidences, 'evidence')
	evidence.text = raw_input("Enter the name of evidance: ")

def gettoolused(root):
    tool_used = SubElement(root, 'tool_used')
    tool = int (raw_input("Select tool uses in murder. 1-Gun 2-Knife 3-Posion"))
    if tool==1:
       Gun = SubElement(tool_used, 'Gun')
       gun_model = SubElement(Gun, 'gun_model')
       gun_model.text = raw_input("Enter Gun model") 
    elif tool==2:
       knife = SubElement(tool_used, 'knife')
       manufacturer_name = SubElement(knife, 'manufacturer_name')
       manufacturer_name.text = raw_input("Enter knife manufacturer name")
    elif tool==3:
       poision = SubElement(tool_used, 'posion')
       name = SubElement(poision,'name')
       name.text = raw_input("Enter poison name")
    else:
        print ("Wrong option selected")

def getkidnappers(root):
    kidnappers = SubElement(root, 'kidnappers')
    no_of_kidnappers = SubElement(kidnappers, 'no_of_kidnappers') 
    no_of_kidnappers.text = int (raw_input("Enter number of kidnappers"))
    mode_of_carry = SubElement(kidnappers, 'mode_of_carry')
    mode_of_carry.text (raw_input("Enter mode used to carry victim"))
                    	    	               	       
print ("Welcome to Crime Reporting System")
crs = open('D:/crs.xml', 'w')
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
	       #robbery = Element('robbery')
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
	
