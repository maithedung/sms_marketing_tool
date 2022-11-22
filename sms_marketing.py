# Importing Twilio API
from twilio.rest import Client

account_sid = "AC411362098e7ba95d3c69e9d27313e9a8"
auth_token = "1836f1a95b821bb2f9e4983433b4eb96"
client = Client(account_sid, auth_token)

message = client.messages.create(
                              body='This is a Demo Text with twilio',
                              from_='+19144605985',
                              to='+84387275685'
                          )

print(message.sid)

# # Reading Massege From Text File
# message = open("message.txt", "r").read()
# contact = open("contact.txt", "r").read().split(',')
#
# # Looping All Number and send Messages
# for x in contact:
#     message = client.messages.create(
#         to=x,
#         from_="+19144605985", # Use your own Number From Twilio
#         body=message)

