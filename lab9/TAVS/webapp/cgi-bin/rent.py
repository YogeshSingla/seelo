#!/usr/bin/python
import cgi
form = cgi.FieldStorage()
print('Content-type: text/html')
# parse form data
# plus blank line
html = """
<TITLE>rent</TITLE>
<H1>Successful</H1>
<HR>
<P>%s</P>
<HR>"""
if not 'cars' in form:
	print(html % 'Invalid')
else:
	print(html % ('Booking %s.' % form['cars'].value))



