import praw 
import time

def bot():
    r = reddit = praw.Reddit(client_id='5OByOST1yzpyHw',
                     client_secret='LX-MwDK405fLHiMYsRmc2kI8Ka0',
                     username='elephantbot',
                     password='redditbot123',
                     user_agent='elephantbot by /u/elephantbot')

    return r 


def output(r):
    for comment in r.subreddit('BotTestingPlace').comments(limit=25):
        if "help" in comment.body:
            print("Comment posted")
            comment.reply("Here are links to donate to elephants!\nhttps://www.sheldrickwildlifetrust.org/donate\nhttp://www.savetheelephants.org/new-donate-page-US/\nhttps://elephantconservation.org/fundraising/donate/")
        print("Loop")
    time.sleep(300)		

r = bot() 
while True: 
    output(r)