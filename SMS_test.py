from twilio.rest import Client

sid = ""
auth_token= ""
client = Client(sid, auth_token)  # twilio client

message = client.messages.create(
    "",
    body ="testing",
    from_= "+12015483972"
)

print(message.sid)
