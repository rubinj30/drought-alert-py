import arrow
import smtplib
from urllib.request import urlopen
import json

gmailPassword = input("What is your gmail password?")

#getting dates for previous 3 days into appropriate format for url request
days_ago_3 = arrow.utcnow().replace(days=-3).format('YYYYMMDD')
days_ago_2 = arrow.utcnow().replace(days=-2).format('YYYYMMDD')
days_ago_1 = arrow.utcnow().replace(days=-1).format('YYYYMMDD')
previous_3_days = [days_ago_3,days_ago_2,days_ago_1]

city = "Marietta"
state = "GA"

listOf3DaysPrecip = []

def pullPrecip():
	for i in previous_3_days:
		data = urlopen(f'http://api.wunderground.com/api/cdc9167d053abdfa/history_{i}/q/{state}/{city}.json')
		json_string = str(data.read(),'utf-8')
		parsed_json = json.loads(json_string)
		#print(json.dumps(parsed_json, indent=4, sort_keys=True)) # No need for, but i like the way it printed out so clearly
		precipi = float(parsed_json['history']['dailysummary'][0]['precipi'])
		listOf3DaysPrecip.append(precipi)

pullPrecip()

totalPrecip = sum(map(float,listOf3DaysPrecip))

if totalPrecip < 0.5:
	smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
	smtpObj.ehlo()
	smtpObj.starttls()
	smtpObj.login('my@email.com', gmailPassword)

	#can use list of strings for multiple email addresses. save as object and replace singular email
	recipients = ['recipient@email.com']
	smtpObj.sendmail('my@email.com',recipients,
	'Subject: Remember to Wather Your Plants\nHello,\n\nIf you are receiving this e-mail, you need to water your plants. The total rainfall from the past few days is:\n' + str(totalPrecip) +' inches\n\nThat is too low, so turn on those sprinklers.')

	#disconnects from server
	smtpObj.quit()
