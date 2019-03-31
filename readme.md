# Progress of the year: Twitter bot

This is a twitter bot fot the "visualizator of the progress of the year" script (https://github.com/MLopezJ/visualizer-of-the-progress-of-the-year)

This bot will tweet everytime the year advances in 1%

## How
Description not available for now. We're working in that.

## Tags

For develop this project, I have followed some previous steps, which I differentiated in tags. Let's see whats each one of the tags mean. (the tags are titled with the "step _ _number__ " format)

### Step 1: Create Twitter bot and checking credentials

To create a bot on Twitter, we need to "ask" first to Twitter if they can give to us permisions. (It's a simple way to see it)

The way we "ask" for that authorization it's by goint to the web page for Twitter developers and sign up as developers. 
> https://developer.twitter.com/en.html

Next we need to press the "create an app" button in the following URL:
> https://developer.twitter.com/en/apps

The system will ask us for some questions that you have to response. Then, click on "create" and then, we already have the permisions for create our twitter bot. (It will be found on "Keys and Tokens" section)

For interact with our Twitter app from Python we are going to use a library that will help in that. It's called Tweepy. You can install typing the next command: 

>python -m pip install tweepy

or just 

> pip install tweepy

Then, we're going to test our credentials by getting basic information of a Twitter account and printig it.  

In getting_started_twitter.py you can see the script and in congif.py you need to put you own credentials provide by Twitter.

## Librarys used

+ Tweepy
    + Let us to manipulate the Twitter APi from Python 

## Environment

* python 3.6.2