import gc
import random
from urllib import urequest
import inky_frame

gc.collect()

URL = "http://localhost:8000/quote.txt"
FILE = "quote.txt"

UPDATE_INTERVAL = 60

gc.collect()  # Claw back some RAM!

quote = []

def update():
    global quote


import requests

# Retrieve the contents of the web page
response = requests.get("http://localhost:8000/quote.txt")

# Check for successful response
if response.status_code == 200:
    # Extract the text
    text = response.text

    # Split the text into lines
    quote = text.split('|')
    quote[2] = quote[2].replace('"""', '"')
    quote[2] = quote[2].replace('""', '"')      

    # Print the only line of text
    print(lines[0])

else:
    print("Error retrieving web page:", response.status_code)

    gc.collect()

def draw():
    graphics.set_pen(1)
    graphics.text(quote[2], 20, 10, WIDTH - 20, 4)
    graphics.set_pen(4)
    graphics.text(quote[3], 40, 300, WIDTH - 20, 4)
    graphics.text(quote[4], 40, 350, WIDTH - 20, 4)
    graphics.set_pen(6)
    graphics.text(quote[0], 500, 350, WIDTH - 20, 4)    
    graphics.update()
