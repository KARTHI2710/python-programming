import datetime
import time
import sys
import os    
while True:
    formatted_time = datetime.datetime.now().strftime("%I:%M:%S %p")
    #sys.stdout.write("\r" + formatted_time)
    #sys.stdout.flush()
    print(formatted_time)
    time.sleep(1)

    
