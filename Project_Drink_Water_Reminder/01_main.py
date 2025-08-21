import time
from pync import Notifier

while True:
     Notifier.notify("Time to drink some water!", title="💧 Hydration Reminder")

     time.sleep(5) # Wait for 3 seconds before the next reminder
