from urllib.request import urlopen
import json
city = "Marietta"
state = "GA"
date = "20170406"
f = urlopen(f'http://api.wunderground.com/api/cdc9167d053abdfa/history_{date}/q/{state}/{city}.json')
json_string = f.read()
parsed_json = json.loads(json_string)
print(json.dumps(parsed_json, indent=4, sort_keys=True))
location = parsed_json['location']['city']
temp_f = parsed_json['current_observation']['temp_f']
print(f"the temperature from {date} in {location} is: {temp_f}")
f.close()
