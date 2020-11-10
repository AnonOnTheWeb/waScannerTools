import feedparser, time, os, sys
from time import strftime

refreshTime = 30 # how often the feed refreshes
ignore_incident = "Burn Off" # define an incident to ignore
currentTime = strftime("%Y-%m-%d %H:%M:%S")
incidentFeed = feedparser.parse("https://www.emergency.wa.gov.au/data/incident_FCAD.rss") # rss feed source
inc = incidentFeed.entries[1]

class ct:
    HEADER = '\033[95m'
    ENDC = '\033[0m'
    RED = '\033[91m'
    YELLOW = '\033[93m'
    GREEN = '\033[92m'
    BLUE = '\033[94m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    incTitle = BOLD + UNDERLINE + RED
    preamble = HEADER + BOLD

def newLine(): # shortcut to print a new line
    print(ct.ENDC + "\r")

def getIncidents(): # print incident information
    for inc in incidentFeed.entries:
        if ignore_incident in inc.title:
            pass
        else:
            print("===========================================================================")
            print(ct.incTitle + inc.title + ct.ENDC) # incident type, location and job number
            print(ct.GREEN + "Incident page: " + inc.link) # link to EmergencyWA page for incident
            print("Incident reported: " + inc.published) # incident creation timestamp
            print(ct.YELLOW + "Coordinates: {} {}".format(inc.geo_lat, inc.geo_long)) # incident coordinates
            print("https://www.google.com/maps/@{},{},15z".format(inc.geo_lat, inc.geo_long)) # incident location via google maps
            print(ct.ENDC + "===========================================================================")

try: # start of program runtime
    while True:
        getIncidents()
        print(ct.preamble + "EmergencyWA active incidents")
        print(ct.preamble + "Current time: " + ct.BLUE + strftime("%Y-%m-%d %H:%M:%S") + ct.preamble)
        print("Current incidents: " + ct.BLUE + str(len(incidentFeed.entries)) + ct.ENDC)
        time.sleep(refreshTime)
        os.system("clear")

except KeyboardInterrupt:
    print(" Terminating..." + ct.ENDC)
    sys.exit()
