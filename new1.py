#currenttime = localtime(time.time())
#print ("current time is ", currenttime)

from datetime import datetime
now = datetime.now()
current_time = now.strftime("%H:%M:%S")
print("Current Time =", current_time)
print("Testing donee for the time, as it is printed")
