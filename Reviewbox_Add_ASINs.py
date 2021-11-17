import requests 
import json
import pandas

#Arrays
servicesList= ['reviewbox', 'copybox', 'pricebox', 'searchbox', 'search']
asinList = []
#Variables
url= 'https://rest.getreviewbox.com/catalog'

#Logic Getting ASIN List 
file = open('text.txt')
for line in file: 
    fields= line.strip().split()
    asinList +=fields

#Logic Updating Reviewbox

data = {'service':servicesList, 'source':'amazon','listing':asinList}       
headers = {'Authorization':'a93d3e91bf32488e9323bf6479ec45f5' }
response = requests.post(url=url,data=data, headers=headers)
dataReports = response.json()