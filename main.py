# company_code_repo
#We realized that we needed to improve our security. You need to register with our company for API access. Sample script below for connecting.
import request
import json

url = 'https://api.piedpipercorporation.com/some/endpoint'
headers = {'content-type': 'application/json','API-ID': 'Your-Application-ID', 'API-KEY': 'Your-API-KEY'}

r = requests.post(url,headers=headers)
