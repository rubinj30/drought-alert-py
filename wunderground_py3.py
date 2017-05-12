import arrow

#getting dates for previous 3 days into appropriate format for url request
days_ago_3 = arrow.utcnow().replace(days=-3).format('YYYYMMDD')
days_ago_2 = arrow.utcnow().replace(days=-2).format('YYYYMMDD')
days_ago_1 = arrow.utcnow().replace(days=-1).format('YYYYMMDD')
previous_3_days = [days_ago_3,days_ago_2,days_ago_1]



from urllib.request import urlopen
import json

city = "Marietta"
state = "GA"

for i in previous_3_days:
    data = urlopen(f'http://api.wunderground.com/api/cdc9167d053abdfa/history_{i}/q/{state}/{city}.json')
    json_string = str(data.read(),'utf-8')
    parsed_json = json.loads(json_string)
#print(json.dumps(parsed_json, indent=4, sort_keys=True)) # No need for, but i like the way it printed out so clearly
    precipi = parsed_json['history']['dailysummary'][0]['precipi']
    print(precipi)
