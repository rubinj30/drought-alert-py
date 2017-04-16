from urllib.request import urlopen
import json
city = "Marietta"
state = "GA"
date = "20170406"
data = urlopen(f'http://api.wunderground.com/api/cdc9167d053abdfa/history_{date}/q/{state}/{city}.json')
json_string = str(data.read(),'utf-8')
parsed_json = json.loads(json_string)
#print(json.dumps(parsed_json, indent=4, sort_keys=True)) # No need for, but i like the way it printed out so clearly
meantempi = parsed_json['history']['dailysummary'][0]['meantempi']
precipi = parsed_json['history']['dailysummary'][0]['precipi']
# using ''' to print just so we can do multi-line statements. 
string_to_print = f'''Date: {date}
City: {city}
Average Temperature: {meantempi} degrees Farenheit
Total Rainfall: {precipi} inches'''
print(string_to_print)
data.close()
#2nd attempt at forking