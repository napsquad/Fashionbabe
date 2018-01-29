from twilio.rest import Client

sid = "ACd0fe40ddfad1dd2313258d175732e860"
auth_token= "7729b923d88c84b4c99921c2cfda0217"
client = Client(sid, auth_token)  # twilio client

message = client.messages.create(
    "+19082794833",
    body ="testing",
    from_= "+12015483972"
)

print(message.sid)