import year_progress  
import draw
import twitter_post   
import time

def process(percent):
    
    progressVar = draw.drawProgress(percent)

    progressVar += ' '+ str(percent)+ '%'

    print(progressVar)

    twitter_post.makePost(progressVar)

progress = 0
oneDay = 24*60*60 # hours * minutes * seconds 

while True:

    actualPercent = year_progress.getYearsProgressPercent()

    if (progress < int(actualPercent)):
        progress = int(actualPercent)
        process(progress)

    time.sleep(7) #oneDay

