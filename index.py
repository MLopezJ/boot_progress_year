import year_progress  
import draw
import twitter_post   
import time

def process(percent):
    
    progressVar = draw.drawProgress(percent)

    progressVar += ' '+ str(percent)+ '%'

    #print(progressVar)

    twitter_post.makePost(progressVar)

progress = 0
oneDay = 24*60*60 # hours * minutes * seconds 
sixHours = 6*60*60

while True:

    actualPercent = int(year_progress.getYearsProgressPercent())

    if (progress < actualPercent):
        progress = actualPercent
        process(progress)

    time.sleep(sixHours)

