# Progress of the year: Twitter bot

This is a twitter bot fot the "visualizator of the progress of the year" script (https://github.com/MLopezJ/visualizer-of-the-progress-of-the-year)

This bot will tweet everytime the year advances in 1%

## How
Description not available for now. We're working in that.

## Tags

For develop this project, I have followed some previous steps, which I differentiated in tags. Let's see whats each one of the tags mean. (the tags are titled with the "step _ _number__ " format)

### Step 1: Create Twitter bot and checking credentials

To create our bot we need to make some things first before program it:
 * Create the bot's twitter account 
 * Register as developer
 * Check credentials

 #### Create the bot's twitter account
 We need a profile where the bot will post the tweets, so we're going to register an account. Go to 
 > https://twitter.com/ 
 
 and signup as usual.  

Then, we are going to register that new twitter account as Developer. 

 #### Register as developer

The developer mode will let us interact with Twitter in a special way, for example, giving the possibility of create apps with the Twitter enviroment. An app will give to us the credetials for creates bots, checks data, and so on. 

So, we're going to sign up in the next link. 
> https://developer.twitter.com/en.html

Next we need to create an app, for that, we need to press the "create an app" button in the following URL:
> https://developer.twitter.com/en/apps

Then, the system will ask us for some questions that you have to response. Then, click on "create" and then, we already have the permisions for create our twitter bot. (It will be found on "Keys and Tokens" section)

#### Check credentials

For interact with our Twitter app from Python we are going to use a library that will help in that. It's called Tweepy. You can install typing the next command: 

>python -m pip install tweepy

or just 

> pip install tweepy

Then, we're going to test our credentials by getting basic information of a Twitter account and printig it.  

In getting_started_twitter.py you can see the script and in congif.py you need to put you own credentials provide by Twitter.

### Step 2: Hello Twitter 

On hello_twitter.py we are going to make our bot's first tweet. For that we are going to use the "update_status ('')" method from tweepy. This method allows us to create a new tweet with the information provyde by in parameters.

You can check the tweet in the twitter profile of the app's owner 

### Step 3: Our application bot 

At this point, we already know how to create a twitter app and make a simple post in our twitter profile with the bot. Now, we are going to add the logic require to know the year's progress in percentage and then, make a post with a progress bar representing the percentage elapsed. Our script will check the progress day by day. So, we can divide all this in the next steps:

* request for the percentage of the year's progress 
    > index.py

* Get the percentage of the year's progress

    > year_progress.py

  If the year has advanced by 1%

    * Draw a progress bar 
        > draw.py

    * Make a post on Twitter 
        > twitter_post.py

* Wait for a day. Repeat. 
    > index.py


## Librarys used

+ Tweepy
    + Let us to manipulate the Twitter APi from Python 
+ Time
    + Its a library for handle time-related tasks. In this case is using for suspends (delays) the execution of the current thread for the given number of seconds
+ Calendar
    + This module allows you to use useful functions related to the calendar. In this specific use case, it is using for get the number of days of a specific month and year
+ Datetime
    + This module supplies classes for manipulating dates and times. Is using for get the current date time  

## Environment

* python 3.6.2