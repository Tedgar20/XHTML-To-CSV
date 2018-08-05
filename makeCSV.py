import sys
import xml.dom.minidom

data=[]
stateCity=state=city=weather=pressure=temperature=humidity=""

document = xml.dom.minidom.parse(sys.argv[1])

#Gather the humidity and pressure
print(sys.argv[1])
table = document.getElementsByTagName('table')[0]

for tr in table.getElementsByTagName('tr'):
    foundHumid = False
    foundPress = False
    for td in tr.getElementsByTagName('td'):
        for node in td.childNodes: #<td> child nodes
            if node.nodeType == 1:
                for nodeChild in node.childNodes: #<b> tag child nodes
                    if nodeChild.nodeValue == "Humidity":
                        foundHumid = True
                        break
                    elif nodeChild.nodeValue == "Barometer":
                        foundPress = True
                        break
            elif foundHumid == True and node.nodeType == 3:
                humidity=node.nodeValue
                foundHumid = False
                break
            elif foundPress == True and node.nodeType == 3:
                pressure=node.nodeValue
                foundPress = False
                break

#Gather the weather
header4 = document.getElementsByTagName('h4')

for h4 in header4:
    if h4.getAttribute("class") == "myforecast-current":
        for node in h4.childNodes:
            if node.nodeType == 3:
                weather=node.nodeValue

#Gather the temperature
header1 = document.getElementsByTagName('h1')

for h1 in header1:
    if h1.getAttribute("class") == "myforecast-current-lrg":
        for node in h1.childNodes:
            if node.nodeType == 3:
                temperature=node.nodeValue

#Gather the state and city
anchor = document.getElementsByTagName('a')

for a in anchor:
    if a.getAttribute("title") != "":
        stateCity = a.getAttribute("title")
        break

#Cleaning up the values
space = pressure.find('i')
pressure = pressure[1:space-1]

humidity = humidity[:(len(humidity)-1)]
#If a state has 0% humidity the website just says % so this chage will make sure it says 0
if len(humidity) == "":
    humidity = "0"

temperature = temperature[:(len(temperature)-2)]

#Philadelphia and Phoenix are handled differently due to how they are named
if ("Philadelphia" in stateCity) == True:
    state = "PA"
    city = "Philadelphia"
elif ("Phoenix" in stateCity) == True:
    state = "AZ"
    city = "Phoenix"
elif ("Houston" in stateCity) == True:
    state = "TX"
    city = "Houston"
else:
    state = stateCity[-2:]
    comma = stateCity.find(',')
    city = stateCity[:comma]

#Getting everything to make a csv
data=[state,city,weather,temperature,humidity,pressure]
print(','.join(data))
