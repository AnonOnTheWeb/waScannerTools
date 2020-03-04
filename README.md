# WA Scanner Tools  
All scripts are written in Python 3.6.9, but **should** run on legacy versions too, with the correct pip packages.  
  
## Released scripts  
### EmergencyWA_Feed  
Small Python script that will check the EmergencyWA incident feed every 30 seconds. Provides the incident creation time and GPS coordinates for the incident. Requires the `feedparser, datetime` pip packages.  
### EmergencyWA_Alerts  
Another Python script that will display basic information about current alerts and advices that have been published, like CAD number and fireground location. Doesn't automatically refresh. Requires same packages as EmergencyWA_Feed.

## TODO  
- ~~EmergencyWA incident feedreader (https://www.emergency.wa.gov.au/data/incident_FCAD.rss)~~  
- ~~EmergencyWA alert feedreader (https://www.emergency.wa.gov.au/data/message.rss)~~  
- Western Power outage feedreader (https://services2.arcgis.com/tBLxde4cxSlNUxsM/arcgis/rest/services/WP_Outage_Prod/FeatureServer/0/?f=json)  
- PagerMon feedreader (https://github.com/pagermon/pagermon)  
- VicEmergency incident feedreader (low priority, https://emergency.vic.gov.au/public/osom-geojson.json)  

## Required pip packages
- feedparser  
- datetime  
- json  
- requests  
  
Contributions and suggestions are welcome!
