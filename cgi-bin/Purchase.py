#!/usr/bin/env python

"""
This is the script
"""
import cgi
import csv

#checks is user is logged in, someone needs to handle changing value of
#field on catalogue.html when the user logs in
def main():
	print "Content-type: text/html\n\n"
	form = cgi.FieldStorage()
	username = form["username"].value
	if username=="default":
		print "<html>\n"
		print" <body>\n"
		print "<h1> ERROR, you are not logged in. Please go back and log in.</h1>\n"
		print "<a href=\"../catalogue.html\">Catalogue Page</a>"
		print "<a href=\"../homepage.html\">Homepage</a>"
		print "</body>\n"
		print "</html>\n"
		sys.exit()
	f = open('../loggedin.csv')
	y = csv.reader(f)
	for row in y:
		for field in row:
			if field == username:
				changeFile()
			else:
				continue
	print "<html>\n"
	print" <body>\n"
	print "<h1>Quantity 1 is", int(form['quantity1'].value), "</h1>\n"
	print "<a href=\"#\" onClick=\"history.go(-1)\">Catalogue Page</a>"
	print "<a href=\"../homepage.html\">Homepage</a>"
	print "</body>\n"
	print "</html>\n"

#this is function to modify Inventory.csv
def changeFile():
	form = cgi.FieldStorage()
	f = open('Inventory.csv')
	csv_f = csv.reader(f)
	rows = list(csv.reader(f))
	#handles Product 1
	if int(form['quantity1'].value) > 0 and int(rows[0][1]) > 0 and form.getvalue('item1'):
		#holds lines
		line_list = []
		r = csv.reader(open('Inventory.csv'))
		lines = [l for l in r]
		with open('Inventory.csv', 'rb') as l:
			line_l = csv.reader(l)
			line_list.extend(line_l)
		line_to_override = {0:['Product 1', int(lines[0][1]) - int(form['quantity1'].value), 5]}
		with open('Inventory.csv', 'wb') as l:
			writer = csv.writer(l)
			for line, row in enumerate(line_list):
				data = line_to_override.get(line, row)
				writer.writerow(data)


		#print lines[0][1]
		#print lines[1][1]
		#print lines[2][1]		
		#print form['quantity1'].value

							
		#new_quant1 = int(lines[0][1]) - int(form['quantity1'].value)
		#new_line = lines[0]
		#new_line[1] = new_quant1
		#print new_line		
	

	#handles Product 2
	if int(form['quantity2'].value) > 0 and int(rows[1][1]) > 0 and form.getvalue('item2'):
		#holds lines
		line_list_two = []
		s = csv.reader(open('Inventory.csv'))
		lines_two = [l for l in s]
		with open('Inventory.csv', 'rb') as l_two:
			line_l_two = csv.reader(l_two)
			line_list_two.extend(line_l_two)
		line_to_override_two = {1:['Product 2', int(lines_two[1][1]) - int(form['quantity2'].value), 4]}
		with open('Inventory.csv', 'wb') as l_two:
			writer_two = csv.writer(l_two)
			for line, row in enumerate(line_list_two):
				data_two = line_to_override_two.get(line, row)
				writer_two.writerow(data_two)

	#handles Product 3
	if int(form['quantity3'].value) > 0 and int(rows[2][1]) > 0 and form.getvalue('item3'):
		#holds lines
		line_list_three = []
		t = csv.reader(open('Inventory.csv'))
		lines_three = [l for l in t]
		with open('Inventory.csv', 'rb') as l_three:
			line_l_three = csv.reader(l_three)
			line_list_three.extend(line_l_three)
	#	print lines_three[2][1]
		line_to_override_three = {2:['Product 3', int(lines_three[2][1]) - int(form['quantity3'].value), 3]}
		with open('Inventory.csv', 'wb') as l_three:
			writer_three = csv.writer(l_three)
			for line, row in enumerate(line_list_three):
				data_three = line_to_override_three.get(line, row)
				writer_three.writerow(data_three)

	
	#item 1 price
	item_1 = int(form['quantity1'].value) * int(rows[0][2])
	item_2 = int(form['quantity2'].value) * int(rows[1][2])
	item_3 = int(form['quantity3'].value) * int(rows[2][2])
	print "<h1> Your total for item one is", item_1 , "</h1>"
	print "<h1> Your total for item two is", item_2 , "</h1>"
	print "<h1> Your total for item three is", item_3, "</h1>"
	print "<h1> Bill Total:", item_1 + item_2 + item_3, "</h1>"
main()

	
