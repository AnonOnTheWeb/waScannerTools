import feedparser # tested and ran on Python 2.7.17
import datetime, time
from time import strftime
from datetime import date

# dict_keys(['title', 'title_detail', 'links', 'link', 'summary', 'summary_detail', 'dfes_region', 'dfes_incidentnumber', 'dfes_publicationtime', 'published', 'published_parsed', 'id', 'guidislink', 'geo_long', 'geo_lat'])

alertFeed = feedparser.parse("https://www.emergency.wa.gov.au/data/message.rss")
alr = alertFeed.entries[1]

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
    for alr in alertFeed.entries:
        print("===========================================================================")
        print(incTitle + alr.title + resetText) # alert title and location
        print(colorText.BOLD + colorText.WARNING + "More information: " + resetText + colorText.BLUE + colorText.UNDERLINE + alr.link + resetText)
        newLine()
        print(colorText.WARNING + colorText.BOLD + "Published at: " + resetText + alr.dfes_publicationtime)
        print(colorText.WARNING + colorText.BOLD + "Incident region: " + resetText + alr.dfes_region) 
        print(colorText.WARNING + colorText.BOLD + "Incident CAD number: " + resetText + alr.dfes_incidentnumber)
        print(colorText.WARNING + colorText.BOLD + "Incident location: " + resetText + alr.geo_lat + ", " + alr.geo_long)
        
        print(resetText + "===========================================================================")
        newLine()

# start of program runtime
getIncidents() # calls the getIncidents function and prints all active incidents

print(preamble + "EmergencyWA current alerts and advices") # print stats message
newLine()

print("Current time: " + colorText.BLUE + strftime("%Y-%m-%d %H:%M:%S") + preamble)
print("Current alerts: " + colorText.BLUE + str(len(alertFeed.entries)) + resetText)
newLine()

resetText
