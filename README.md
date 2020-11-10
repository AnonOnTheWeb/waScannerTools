# WA Scanner Tools  
All scripts are written in Python 3.6.9, but **should** run on legacy versions too, with the correct pip packages.  
  
## Released scripts  
### EmergencyWA_Feed  
Small Python script that will check the EmergencyWA incident feed every 30 seconds. Provides the incident creation time and GPS coordinates for the incident. Requires the `feedparser` pip packages. The `EmergencyWA_FeedCompact` is similar, but puts all details on one line.  
### EmergencyWA_Alerts  
Another Python script that will display basic information about current alerts and advices that have been published, like CAD number and fireground location. Doesn't automatically refresh. Requires the `feedparser` pip packages. 

## TODO  
- ~~EmergencyWA incident feedreader (https://www.emergency.wa.gov.au/data/incident_FCAD.rss)~~  
- ~~EmergencyWA alert feedreader (https://www.emergency.wa.gov.au/data/message.rss)~~  
- Western Power outage feedreader (https://services2.arcgis.com/tBLxde4cxSlNUxsM/arcgis/rest/services/WP_Outage_Prod/FeatureServer/0/?f=json)  
-  Water Corperation outages (https://www.watercorporation.com.au/gss/events?ts and https://www.watercorporation.com.au/gss/events?ts)  
- PagerMon feedreader (https://github.com/pagermon/pagermon)  
- VicEmergency incident feedreader (low priority, https://emergency.vic.gov.au/public/osom-geojson.json)  
  
Contributions and suggestions are welcome!
