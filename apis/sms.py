import africastalking
africastalking.initialize(
    username="kimtai",
    api_key="a5c11f56c5829ef6960a7"
)
sms = africastalking.SMS
def send_sms(message, phone_numbers): 
    sender = "OLMISMISFCS"
    try:
        response = sms.send(message, phone_numbers, sender)
        print(response)
    except Exception as error:
        print("Error is ", error)
	
