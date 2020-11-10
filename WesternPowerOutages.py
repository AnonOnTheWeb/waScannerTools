import requests, urllib3
urllib3.disable_warnings()

endpoint = "https://services2.arcgis.com/tBLxde4cxSlNUxsM/arcgis/rest/services/WP_Outage_Prod/FeatureServer/0/query?where=1=1&outFields=*&returnGeometry=false&f=json"

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

def getAllOutages():
    response = requests.get(endpoint, verify=False)
    print("Reported outages: {}".format(len(response.json()["features"])))
    for outage in (response.json()["features"]):
        if outage["attributes"]["PLANNEDOUTAGE"] == "Planned":
            printOutage(type="planned", inc_ref=outage["attributes"]["INCIDENTREF"], out_type=outage["attributes"]["PLANNEDOUTAGE"], cus_imp=outage["attributes"]["NOCUSTOMERSIMPACTED"], aff_area=outage["attributes"]["AFFECTED_AREA"], st=outage["attributes"]["OUTAGESTARTTIME"], et=outage["attributes"]["ESTIMATEDRESTORATIONTIME"], n=outage["attributes"]["Tags"])
        else:
            printOutage(type="unplanned", inc_ref=outage["attributes"]["INCIDENTREF"], out_type=outage["attributes"]["PLANNEDOUTAGE"], cus_imp=outage["attributes"]["NOCUSTOMERSIMPACTED"], aff_area=outage["attributes"]["AFFECTED_AREA"], st=outage["attributes"]["OUTAGESTARTTIME"], et=outage["attributes"]["ESTIMATEDRESTORATIONTIME"], n=outage["attributes"]["Tags"])

def printOutage(type, inc_ref, out_type, cus_imp, aff_area, st, et, n):
    if type == "planned":
        print("===========================================================================" + ct.GREEN)
        print("Incident number: {}".format(inc_ref))
        print("Outage type: {}".format(out_type))
        print("Customers impacted: {}".format(cus_imp))
        print("Affected region: {}".format(aff_area))
        print("Outage start: {}".format(st))
        print("Estimated restore time: {}".format(et))
        print("Additional notes: {}".format(n))
        print(ct.ENDC + "===========================================================================")
    if type == "unplanned":
        print("===========================================================================" + ct.YELLOW)
        print("Incident number: {}".format(inc_ref))
        print("Outage type: {}".format(out_type))
        print("Customers impacted: {}".format(cus_imp))
        print("Affected region: {}".format(aff_area))
        print("Outage start: {}".format(st))
        print("Estimated restore time: {}".format(et))
        print("Additional notes: {}".format(n))
        print(ct.ENDC + "===========================================================================")

getAllOutages()
