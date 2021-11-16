import requests
import json
from requests import api 
import urllib3 
import logging 
import boto3
import os 


# Overall process 
# Step 1: Create an Array containg the last 90days dates.
# Step 2: Create an Array containing the clients. 
# Step 3: Create a For Loop to run through the clients array
#       Step 3.5: Create a For Loop to run through the dates array
#        Step 3.7 ForEach Client run through Date Array
#                 In Date Array send download this export file for tis.   
# Step 2: Connect to RB  
# Step 2: Create a for loop for to loop through the array. 
#          ForEach Date send this export to S3.  
# Connect to Reviewbox 
   # Change the Buybox Export with  the array, create a for loop to run through the array. 
# For each 

# Parts 

##Arrays
dateRange= ['1636934400','1636848000','1636761600','1636675200','1636588800','1636502400','1636416000','1636329600','1636243200','1636156800','1636070400','1635984000','1635897600','1635811200','1635724800','1635638400','1635552000','1635465600','1635379200','1635292800','1635206400','1635120000','1635033600','1634947200','1634860800','1634774400','1634688000','1634601600','1634515200','1634428800','1634342400','1634256000','1634169600','1634083200','1633996800','1633910400','1633824000','1633737600','1633651200','1633564800','1633478400','1633392000','1633305600','1633219200','1633132800','1633046400','1632960000','1632873600','1632787200','1632700800','1632614400','1632528000','1632441600','1632355200','1632268800','1632182400','1632096000','1632009600','1631923200','1631836800','1631750400','1631664000','1631577600','1631491200','1631404800','1631318400','1631232000','1631145600','1631059200','1630972800','1630886400','1630800000','1630713600','1630627200','1630540800','1630454400','1630368000','1630281600','1630195200','1630108800','1630022400','1629936000','1629849600','1629763200','1629676800','1629590400','1629504000','1629417600','1629331200','1629244800','1629158400','1629072000','1628985600','1628899200','1628812800','1628726400','1628640000','1628553600','1628467200','1628380800','1628294400','1628208000','1628121600','1628035200','1627948800','1627862400','1627776000','1627689600','1627603200','1627516800','1627430400','1627344000','1627257600','1627171200','1627084800','1626998400','1626912000','1626825600','1626739200','1626652800','1626566400','1626480000','1626393600','1626307200','1626220800','1626134400','1626048000','1625961600','1625875200','1625788800','1625702400','1625616000','1625529600','1625443200','1625356800','1625270400','1625184000','1625097600']

clientDictionary = {'acme':'88221f2419dd4d4b85b21b35ca222a24','annin':'f5ebfa85c8c542f496669e307456bcf4','behrens':'ae01ea747f2d4ed4952c65def31bc85d','coldpruf_indera':'bfd2ca2789f3427c822e1001715df904','f_bodyglove':'797d4ff273a446fe85dd4ab4d70c50a2','f_officeproducts':'','franklininternational':'442cee4a3c4a497da87096f21d50e90b','grassworx':'80856637b0c240fe9860a534b9d1da85','optimus':'3d9c682c474c4a45ae530011362fcbd9','papermart':'c98c8b87f3804761a6d7cf96dc81923a','performbetter':'9c527e6373534d1d9a0c40c437075b22','radiant_therapeutics':'28b5d6d121014c63996293f8a4939deb','samsill':'4b4b42583b6246708d9452bab14725d6','sgs':'170f070a0d27461985e37a08d03d8bec','touchjet':'4fd6ad38d33d430ab256841a8d709656','whynter':'c1069350513d495d82cb93dc7d741770','mcsframe':'2f4d6ef510024b59bca46048efbf4a79','customaccessories':'2528db257e274a5681f24f8eb1ab977a','mepra':'9b9753451b18415185568c5a138aa62b','orcapacific_busdev':'63e9efbb323a418e9f3c5707fbe86fdc','marcraft':'63c526943d994678a88f85579657e902','hilco':'88a91cc7099c412f821d9b80bdf7545b','educators_resource':'268e85c732e44448ac23a595e6205bcb','orcapacific_busdev2':'c1cb7e334d8242b3a3520b942a35e7ec','summit_brands':'5048da911ab2487bbec80ac9db061562','herbaceuticals':'c4370c01973647fa8905e8bbbaa4d66b','scosche':'83cea7ddaeba4112859ac8afe572e58b','orcapacific_busdev3':'12d4ca49e07d499e9768b7d19d20d92a','godivachocolates':'8e1a45f801204c68b3ea08467103d519','amctheaters':'ac26700b80784c2494a2783052c70e2d','orcapacific_busdev4':'168f36f7434a44739fc958a199b09421','vida':'b42a1b05c0de4803bc26b057cfae64ce','kenroyhome':'fd546795374a4c78a0c874187b862a94','rangeready':'9ab583815f9049f7a4950bed31d1090b','pkgrills':'32bbb58c17ce4ec094185f37f4f9d106','superfeet':'3701523b5a2f437eae36bdaf11550252','bekinaboots':'d64f7f6f156346c78bebe50886d5efe7','healthypet':'f7be69ac290b498582faab24a1cb887b','hunterfan':'9c2429d4fda04758ba26930f25c0b27a','mindray':'642ff8783c2d4a3ca5a4055f0f4a22bd','orcapacific_busdev5':'c88910b54b8b40599c47492e6cd22203','orcapacific_busdev6':'cec9709299ba4931bd7b68e6b7671102','primetimepackaging':'d0da775946904aeebcafbe39f3b759a9','landau1':'d7276e909f1c4f33877f4602358e478f','gerberplumbing':'2e7898c169f44fa49368bac73ad46e0d','planbased':'928c2b48ecb3464d86880d65b83f5f2b','chandler4corners':'836d8270cb7f4ed18cedb22b6c54f088','foodmatch':'c558cddd19cc4246a652ca668bba5f1e','s&r_sports':'5e6643ea313c4243833b8d61f923dbc0','soho_management':'19524106df404618b75c829b3be90761','prospects_dm':'aed1db09d10549e98a65d20fe38b86d5','darwins_pet':'0abb93b278a646a1a91bfda2343d3d50','sci':'feff929f776a4fd9b7a94f3853845659','aet_systems':'4112144e5e134d4583552e7d6f557da2','blue_bottle_coffee':'bbc30896a8d3419389046a25fa816bf6','medology':'1e67ae722d0246788aebf77d44114289','riifo':'9c81abbe67bf43acbac0607dd6f54661','rst':'8f286b7c733b40528f6320fe9b045125','rinnai':'ea9806c206fd4b6185dcbd78caeca096','ibb':'49215ef81be14abbb697f9ad16cd9260','kenroy_home_ca':'be85a3bb7816425390d1de80195a8351','acme_canada_first_aid':'05bb7f0fe9cf4a1a88439d9930a0288a','sam_villa':'c6059cbe1db5453abfc46015e4b6ffeb','brookwood_capital':'bcc0f76674f7404e9efee9f40a806a4e','glue_dots':'6ce2b8f7e7674a28bb6cda9cfde6cd2c','bsm':'0ac40b75916d4e2fb945b7c2eca07250','basf':'20e2ff63e5344599b382840aee64b014','trend_marketing':'06745250bb5c4dc695e0a27458ccfc1d','seco_tools':'a28d776e9bad4580b3f580abcef0ed5d','kyocera':'54d4fae0ae8344b8bb66ac60084c3d6f','colosseum_athletics':'f68710d11e1a4cc5a003acf679c96cd7','silk_spice':'ce74d8012c534a91a6bbcfb7dd64fa20','edge_sports':'09c6c0a2c47a4d80ae41c70681f3fcd4','moda_import':'abee79246f6246a49a9da46b71654edd','core_pacific':'b8c86091775d4efebc50eff8e7ff6f45','plume_science':'65cc29db21aa4015a922d78e6de38fbd','group_iii':'d55ff427913a4759926b17bef004d16e','pacers_running':'00800760460e4667aa7875b34979d0c9','giant_hoodies':'5b18a51e6e074b2a98a60945bca43436','izzo_golf':'8f95dc65e43c4d3e894f8d74d02a8aa1','maui_jim':'a59ae00d091e44448ea05661bfce7b9c','trulyfe':'b348b21fc1a8442ba58c77a9a1cabc6c','ekco':'f5a074a905744ad291fb9bb150a0beda','calmigo':'4e3c2ec8c6cf4f24ae16527404cedd54','bodyrock':'77bbca5d212442e8a4ae5db6b4ae068c','jaxco':'7bebd538d0064f9bad3920c9cb19c290','premier_accessory_group':'c55e7909984e4f1cb1b1f3bbbd72cf90','instanatural':'69e23bda127d4bfa967db2240c681b56','kids_n_such':'f437a809ac3a4ceea3480062715414c2','juniper_compounds':'d8488791a8ae43c8a854362ed52aa556','pts_america':'40fdf49ebe2f43ba8a3a2ad6cb3f368c','old_school_beverages':'e10168ddf6314211b63cae00743a6799','philips':'dd2b9f2653eb4385914887fd489012e2','briskheat':'8a42d17cabdf4bd5993bbb05545c011c','fowler':'f2ba9f3dacf04fa9bf3c7bd7528f69b6','luglife':'8101c97fe51440b68e45d500f4c38bb5','wh_buyer':'3725a813f20b4cf59d6bb51503743ee9','fgx':'bb4e75dbaf964301aac78316b2a7ae53','pristine_hd':'8029ec719d9144248e7bae9075659168','drive_medical':'41d52f84d9a4431494fa594e624f56a1','rritual':'8e2f50f713834c77816d27e51cee34f7','zing':'56b8baa2b784417fbaea99c7e3d89f9f','bradley_smoker':'c845886721c94d798019793a5bf99f7e','tastefully_simple':'121b6d97be79457aa0f3bf74e2e3b586','led_technologies':'f437ef9cf5324b5ba4fbea6026548a12','casetify':'e503ef321af84d97a2d1c010380e4bc3','groupe_chantelle':'1b0951004c6e451c967b0dbd91a1f109','karcher':'5c01f65797464b7ca63d02d574b7a983','verbatim':'90811dfec7194f5ca859a2b9a5c98e6b','tenga':'a1f815bbd9834b6da770d9cadff0f8f0','ideal_security':'29a442b999d546b1a8ee11c42091313b','health_thru_nutrition':'1b7379a2602648e49146bdcebe979e9a','suessie':'c30dd65ae1e74f16b2eed854e6d142e7','bay_valley_foods':'70db2199ac7f4e8387645b92aa86360c','revel_nail':'f9afbf5fc8b04c00b638c73e64f5ae99','fit_my_foot':'a5a34458c2d14b5ab9e89759d370f776','perfume_worldwide':'3924f9ecf93548bfa728adfefe3e4c74','the_gulati_group':'772842ec3e5846c69b71ed97a27410c6','code_1_supply':'11f945c7dddf404585dcd49a316a1b6e','jaanuu':'5c3e6b99ae63428996f8efdee6d10e0a','system_three_resins':'316d7b70a10747098bcef5b94fa09824','jurlique_holistic_skincare':'23552be92f0540b9ad4bab9087dfa6bf','bloomage_biotechnology':'b08d9514ea3749fe8d2361b2feb14b7a','jockey_international':'0a10e78130c84e43a4c3e5280be71b1b','word_on_fire':'396e2be42255421398e6888e6bb1df47','linxup':'449dc38201654bd18d491a92efed496c','simplified_it_products':'39f0e76b8afb43d5abc863f0c3d72726','keune':'275abdfdb203414993d90a98b9233f8b','deer_stags':'829b5877cd3b4819b4a5b48f6267dcb3','bravus':'af7bd90264cd4a24844a55c4a9c63989','glo_science':'1da703f9678940a89e06882bdc9d7ae8','inglesina':'f998c39d0aee453389c4b6d35bf382d4','promix_nutrition':'ed54f6870f89404da33fb0b8545941b6','orcapacific_demo':'20c5f447d6cf4ff78e65751dc5173ba4','viridian_weapon_tech':'a4bdbdcb6fdd4ae8916d2fd82bcaf9db','linksmed':'2a2fe11a83094b52b15dbd3c7244f79e','marimekko':'855e6b978ae04f7390fb2eef7409100d','electrolux':'e1d46b9d148f4a40870050e0823b1439','viome':'718ab5d0df394e45a132364c383767e9'}
clientDictionary2 = {'neato':'a93d3e91bf32488e9323bf6479ec45f5'}
##Variables
StartDate= '1636934400'
EndDate = '1625097600'


#Step 1 Request Report

# data = {'type':'BuyboxExport', 'name': 'Bruder_BuyboxExport','bucket':'orcacarbondata','start_ts':StartDate, 'end_ts':EndDate}
# headers = {'Authorization': 'a66d68cd8fef49689186856013ebefdf'}
# url = 'https://rest.getreviewbox.com/report'
# response = requests.post(url=url,data=data, headers=headers)


# with open(response.json()):
#    data=json.load()
# print(response)
# print(response.json())
# responseInfo= json.loads(response.read())

# print(responseInfo)
# Step1.5 get the JSON ID
# # 
# print(response.json())
# resp_str =response.json()

# jobid= json.loads(resp_str)
# print(jobid)


# Step 1.6 Get the job id and place into job variable

#Step 2 Get Report

url = 'https://rest.getreviewbox.com/job'
headers = {'Authorization': 'a93d3e91bf32488e9323bf6479ec45f5'}
params= {'job':'5e55d20d-0cd8-4b10-a367-c85c7beb6e4e'}
response = requests.get(url, params=params, headers=headers)
print(response.json())


# print(response.json())
# print(response)
# # print(response.json())

# ## Logic 

# ### Step 1: Iterate through the Dates ~ For Each Date in the dateRange Array do reques
# #  Step 1.5 te through the ClientDictionary ~ For each client request the report 
# # For each client get  

reportArray=['BulkReviewsExport', 'BulkQuestionsExport','BuyboxExport', 'SellerPricesExport','CopyboxContentExport', 'SearchRankExport']

# for reports in reportArray:
#        for autho in clientDictionary2.values():
#           for clients in clientDictionary2:
#               data = {'type':reports, 'name': str.capitalize(clients)+'_'+reports,'bucket':'orcacarbondata','start_ts':StartDate, 'end_ts':EndDate}       
#               headers = {'Authorization': autho}
#               url = 'https://rest.getreviewbox.com/report'
#               response = requests.post(url=url,data=data, headers=headers)
#              # print(reports, autho, response.json())
#               dataReports =response.json() ##Need to pull job values out of JSON 
#               print(dataReports)
#             #  job= json.dumps(job)


# #Step 2            #  print(job)
# for autho in clientDictionary2.values():
#        for status, jobid in dataReports.items():
#           print(jobid)
# #           url = 'https://rest.getreviewbox.com/job'
#           headers = {'Authorization':autho}
#           params= {'job':jobid}
#           response = requests.get(url, params=params, headers=headers)
#           print(jobid, response.url)
# # for reports in reportArray:

# #BuyBoxData

## Get Data Request API

# for dates in dateRange:
#    for reports in clientDictionary.values():
#       data = {'type':'BuyboxExport', 'name': '_BuyboxExport','bucket':'orcacarbondata','start_ts':dates, 'end_ts':dates}
#       headers = {'Authorization': reports}
#       url = 'https://rest.getreviewbox.com/report'
#       response = requests.post(url=url,data=data, headers=headers)
#       print(dates,reports, response.json())

# clientAPIs = clientDictionary.items

# for item in clientAPIs:
#    print(item)
   
# for dates in dateRange:

#Step 2
# url = 'https://rest.getreviewbox.com/job'
# headers = {'Authorization': 'dd2b9f2653eb4385914887fd489012e2'}
# params= {'job': '9252a8b1-05b8-415f-a345-aab964c930be'}
# response = requests.get(url, params=data, headers=headers)
# print(response)
# url= 'https://rest.getreviewbox.com/'
# apiKey ='dd2b9f2653eb4385914887fd489012e2'

#Step 3: Download the file 
#response= request.get("",headers=headers)
# with urllib3.request.urlopen("")
# data = json.load(url.read().decode())

