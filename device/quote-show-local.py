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

    # Read the quote from the file
    try:
        with open(FILE, 'r') as f:
            contents = f.read()
            # Split the contents on the '|' character
            quote = contents.split('|')
            quote[2] = quote[2].replace('"""', '"')
            quote[2] = quote[2].replace('""', '"')            
    except FileNotFoundError as e:
        print(e)

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

