import arrow
import smtplib
from urllib.request import urlopen
import json

gmail_password = input("What is your gmail password?")

# getting dates for previous 3 days into appropriate format for url request
days_ago_3 = arrow.utcnow().replace(days = -3).format('YYYYMMDD')
days_ago_2 = arrow.utcnow().replace(days = -2).format('YYYYMMDD')
days_ago_1 = arrow.utcnow().replace(days = -1).format('YYYYMMDD')
previous_3_days = [days_ago_3, days_ago_2, days_ago_1]

city = "Atlanta"
state = "GA"

list_3_days_precip = []

def pull_precip():
	for i in previous_3_days:
		data = urlopen(f'http://api.wunderground.com/api/cdc9167d053abdfa/history_{i}/q/{state}/{city}.json')
		json_string = str(data.read(),'utf-8')
		parsed_json = json.loads(json_string)
		precipi = float(parsed_json['history']['dailysummary'][0]['precipi'])
		list_3_days_precip.append(precipi)

pull_precip()

total_precip = sum(map(float,list_3_days_precip))

if total_precip < 0.5:
	smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
	smtpObj.ehlo()
	smtpObj.starttls()
	smtpObj.login('my@email.com', gmail_password)

	#can use list of strings for multiple email addresses. save as object and replace singular email
	recipients = ['recipient@email.com']
	smtpObj.sendmail('my@email.com',recipients,
	'Subject: Remember to Wather Your Plants\nHello,\n\nThere has only been ' + str(total_precip) + ' inches of rainfall in the past few days. Make sure to water your plants.')

	#disconnects from server
	smtpObj.quit()
