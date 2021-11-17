import requests 
import json

#Arrays
servicesList= ['reviewbox', 'copybox', 'pricebox', 'searchbox', 'search']

#Variables
url= 'http POST https://rest.getreviewbox.com/catalog 

#Logic 

  data = {'type':reports, 'name': 'Neato'+'_'+reports,'bucket':'orcacarbondata','start_ts':StartDate, 'end_ts':EndDate}       
   headers = {'Authorization':'a93d3e91bf32488e9323bf6479ec45f5' }
   url = 'https://rest.getreviewbox.com/report'
   response = requests.post(url=url,data=data, headers=headers)
   dataReports = response.json()