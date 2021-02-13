#!/usr/local/bin/python3

from cgitb import enable
enable()

from cgi import FieldStorage

from html import escape

print('Content-Type: text/html')
print()
unitSet = ["inches","feet","yards"]
form_data = FieldStorage()
length = (form_data.getfirst('length', ''))
units = form_data.getfirst('units', '').strip()
outcome = ""
try:
    length = float(length)
    #unit == 'inches' or unit == 'feet' or unit == 'yards'
    inchesOutput = 0
    feetOutput = 0
    yardsOutput = 0
    unitFlag = True
    if units == 'inches':
        inchesOutput = length
        feetOutput = length / 12
        yardsOutput = length / 36
    elif units == 'feet':
        inchesOutput = length * 12
        feetOutput = length 
        yardsOutput = length / 3
    elif units == 'yards':
        inchesOutput = length * 36
        feetOutput = length * 3
        yardsOutput = length
    else:
        outcome = """This unit of measurment has not been accounted for.
                        Please try again."""
        unitFlag = False
    if unitFlag == True:
        outcome = """
            <table>
                <tr>
                    <th>Inches</th><td>%.2f</td>
                </tr>
                <tr>
                    <th>Feet</th><td>%.2f</td>
                </tr>
                <tr>
                    <th>Yards</th><td>%.2f</td>
                </tr> 
                    </table>""" % (inchesOutput, feetOutput, yardsOutput)
except:
	outcome = "You have entered something I cannot process. Please try again"

print("""
    <!DOCTYPE html>
    <html lang="en">
        <head>
            <meta charset="utf-8" />
            <title>Lengths</title>
            <link rel="stylesheet" href="styles.css" />
        </head>
        <body>
            %s
        </body>
    </html>""" % (outcome))

