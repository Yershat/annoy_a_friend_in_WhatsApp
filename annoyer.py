## Simple app to annoy someone on WhatsApp

import pyautogui as pt
import time

limit = input("Enter limit: ")
message = input("Message: ")
i = 0

time.sleep(3)

while i < int(limit):
    pt.typewrite(message)
    pt.press("enter")

    i+=1


# After running the code, just press on Enter the message on WhatsApp