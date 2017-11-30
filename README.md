# drought-alert-py

## Uses:
This uses wunderground API to gather recent rainfall in specified area and alerts user when they need to water their plants.

Best to be setup to run on a daily basis via Windows Task Manager or Chron on Mac, but the version I've included requests an e-mail password as input. 

## To get working:
Update the e-mails that it will send from and include e-mails to be sent to as the 'recipients'.
To get working automatically, update the password from requested input. 

## Prerequisites:
 - Python 3.6 (because of f-strings)
 - weather underground API key (anvil plan)[https://www.wunderground.com/weather/api/]

