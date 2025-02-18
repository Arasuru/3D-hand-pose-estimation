from datetime import datetime
import random

gestures = ["thumbs up", "peace", "ok sign", "open palm", "pointing finger"] * 3

activities = ["pouring water", "writing", "moving an object", "opening a jar/bottle", "handshaking", "using controller"] 

starttime = datetime.now().timestamp()
while(True):
    input("enter any key")
    if(activities != [] or gestures != []):
        cat = random.choice([gestures, activities])
        if (cat != []):
            choice = random.choice(cat)
            print("selected activity: ", choice)
            cat.remove(choice)
    else:
        break    
        
