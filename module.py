import onevizion
import json

with open('settings.json', 'rb') as PFile:
 settings = json.loads(PFile.read().decode('utf-8'))

try:
  OvAccessKey = settings['OvAccessKey']
  OvSecretKey = settings['OvSecretKey']
  DOMAIN =settings['OvDomainName']  
except Exception as e:
	raise "Please check settings"

Req = onevizion.Trackor(trackorType = 'USERS', URL = DOMAIN, userName=OvAccessKey, password=OvSecretKey, isTokenAuth=True)
Req.read(filters = {'POC_POSITION2':'Хокимият'}, 
		fields = ['TRACKOR_KEY','XITOR_KEY_ALT1','POC_POSITION2'], 
		sort = {'TRACKOR_KEY':'ASC'}, page = 1, perPage = 1000)
for rec in Req.jsonData:
  updateFields = {}
  updateFields['POC_POSITION_USER'] = 'Тест'
  Req.update(filters = {'TRACKOR_ID': rec['TRACKOR_ID']}, fields = updateFields)

