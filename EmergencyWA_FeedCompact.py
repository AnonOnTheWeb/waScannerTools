import feedparser, time, os
from time import strftime
from sys import exit

refresh_time=30 # how often the feed refreshes
ignore_incident="Burn Off" # incident to ignore
current_time = strftime("%Y-%m-%d %H:%M:%S")
incident_feed = feedparser.parse("https://www.emergency.wa.gov.au/data/incident_FCAD.rss") # rss feed source
inc = incident_feed.entries[1]

class ct:
    HEADER = '\033[95m'
    ENDC = '\033[0m'
    RED = '\033[91m'
    YELLOW = '\033[93m'
    GREEN = '\033[92m'
    BLUE = '\033[94m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    INCTITLE = BOLD + UNDERLINE + RED

def newLine(): # shortcut to print a new line
    print(ct.ENDC + "\r")

def getIncidents(): # print incident information
    for inc in incident_feed.entries:
        if ignore_incident in inc.title:
            pass
        else:
            print(ct.INCTITLE + inc.title + ct.ENDC + ct.YELLOW + " | Reported: " + inc.published + ct.ENDC + ct.BLUE + " | Location: " + inc.geo_lat + "," + inc.geo_long)
# start of program runtime
try:
    while True:
        getIncidents() # recursively print all active incidents
        time.sleep(refresh_time)
        os.system("clear")

except KeyboardInterrupt:
    newLine()
    print(ct.GREEN + ct.BOLD + "Terminating...")
    ct.ENDC
    exit()
