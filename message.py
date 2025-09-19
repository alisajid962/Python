import pywhatkit as kit
import time

phone_number = "+923043786433"
message = "Hello! This is an automated message sent multiple times."

# Get current time
current_hour = time.localtime().tm_hour
current_minute = time.localtime().tm_min   # start 1 minute from now

# Send message 20 times
for i in range(20):
    kit.sendwhatmsg(phone_number, message, current_hour, current_minute + i)
    print(f"Message {i+1} scheduled for {current_hour}:{current_minute + i}")
    time.sleep(5) 
