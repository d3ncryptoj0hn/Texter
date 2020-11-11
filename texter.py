#!/bin/python3
#re-write by johnsmith80
#edited
#code owner: https://www.twilio.com

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    CVIOLET = '\33[35m'

from twilio.rest import Client

account_sid = '' # Found on Twilio Console Dashboard = account_sid
auth_token = '' # Found on Twilio Console Dashboard = auth_token

myPhone = '' # Phone number you used to verify your Twilio account = real_number
TwilioNumber = '' # Phone number given to you by Twilio = provided phone number_by_twilio

client = Client(account_sid, auth_token)
print(bcolors.OKGREEN + '''
 [------------------------------------------]
{|    _____ _______  _______ _____ ____     |}
{|   |_   _| ____\ \/ /_   _| ____|  _ \    |}
{|     | | |  _|  \  /  | | |  _| | |_) |   |}
{|     | | | |___ /  \  | | | |___|  _ <    |}
{|     |_| |_____/_/\_\ |_| |_____|_| \_\   |}
{|                                          |}
 [------------------------------------------]

					sign: Default
''')
print("")
print('From=	'+ TwilioNumber)
target = input("Target: ")
body = input("Message: ")
time = int(input("Number of SMS: "))

print(bcolors.CVIOLET + "")
for i in range(time):
	print("~> " + bcolors.WARNING + bcolors.BOLD + target + " Targeting...")
	client.messages.create(
	  to=myPhone,
	  from_=TwilioNumber,
	body= body)

print(bcolors.BOLD + bcolors.OKBLUE + '''
			!!!Message Send!!!
''' + bcolors.ENDC)
