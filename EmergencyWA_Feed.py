import feedparser # tested and ran on Python 2.7.17 and 3.6.9
import datetime, time # script will automatically refresh every 30 seconds, newest incidents are pushed to the bottom of the list, and older incidents are further up
from time import strftime
from datetime import date

incidentFeed = feedparser.parse("https://www.emergency.wa.gov.au/data/incident_FCAD.rss")
inc = incidentFeed.entries[1]

class colorText:
    HEADER = '\033[95m'
    ENDC = '\033[0m'
    EMERGENCY = '\033[91m'
    WARNING = '\033[93m'
    GREEN = '\033[92m'
    BLUE = '\033[94m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

currentTime = strftime("%Y-%m-%d %H:%M:%S")
incTitle = colorText.BOLD + colorText.UNDERLINE + colorText.EMERGENCY
preamble = colorText.HEADER + colorText.BOLD
resetText = colorText.ENDC

def newLine(): # shortcut to print a new line
    colorText.ENDC
    print("\r")

def getIncidents(): # print incident information
    for inc in incidentFeed.entries:
        print("===========================================================================")
        print(incTitle + inc.title + resetText) # incident type, location and job number
        print(colorText.GREEN + "Incident page: " + inc.link) # link to EmergencyWA page for incident
        print("Incident reported: " + inc.published) # incident creation timestamp
        newLine()
        print(colorText.WARNING + str(inc.summary) + colorText.GREEN) # incident summary
        newLine()
        print("Coordinates: " + inc.geo_lat + " " + inc.geo_long) # incident coordinates
        print("Map: https://www.google.com/maps/@" + inc.geo_lat + "," + inc.geo_long + ",15z") # incident location via google maps
        print(resetText + "===========================================================================")
        newLine()

# start of program runtime
while True:
    getIncidents() # calls the getIncidents function and prints all active incidents
    print(preamble + "EmergencyWA active incidents") # print stats message
    newLine()
    print("Current time: " + colorText.BLUE + strftime("%Y-%m-%d %H:%M:%S") + preamble)
    print("Current incidents: " + colorText.BLUE + str(len(incidentFeed.entries)) + resetText)
    newLine()
    time.sleep(30)

resetText
