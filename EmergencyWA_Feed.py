import feedparser # tested and ran on Python 2.7.17
import datetime, time
from time import strftime
from datetime import date

debugMode = False # toggle debug mode (True or False)

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

def debug(): # debug output function
    print("Current time: " + currentTime)
    print("Incident feed keys: " + str(inc.keys()) + "\n")
    print(str(inc) + "\n")
    print(inc.version)
    print("\n")

def getIncidents(): # print incident information
    for inc in reversed(incidentFeed.entries):
        print("===========================================================================")
        print(incTitle + inc.title + resetText) # incident type, location and job number
        print(colorText.GREEN + "Incident reported: " + inc.published) # incident creation timestamp
        newLine()

        print("Coordinates: " + inc.geo_lat + " " + inc.geo_long) # incident coordinates
        print("Map: https://www.google.com/maps/@" + inc.geo_lat + "," + inc.geo_long + ",15z") # incident location via google maps
        newLine()

        print("Incident page: " + inc.link) # link to EmergencyWA page for incident
        print(resetText + "===========================================================================")
        newLine()

# start of program runtime

if debugMode == True:
    print("Debug mode enabled")
    debug() # output the debug info if True

getIncidents() # calls the getIncidents function and prints all active incidents

print(preamble + "EmergencyWA active incidents") # print stats message
newLine()
print("Current time: " + colorText.BLUE + currentTime + preamble)
print("Current incidents: " + colorText.BLUE + str(len(incidentFeed.entries)) + resetText)
newLine()

resetText