import praw
import enchant

client_id = "add here"
client_secret = "add here"
username = "add here"
password = "add here"
user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"

reddit = praw.Reddit(client_id = client_id,
                     client_secret = client_secret,
                     username = username,
                     password = password,
                     user_agent = user_agent)

target_sub = "FreeKarma4U"
subreddit = reddit.subreddit(target_sub)

trigger_phrase = "upvote"

d = enchant.Dict("en_US")

for comment in subreddit.stream.comments():

    word = comment.body.replace(trigger_phrase, "")

    reply_text = "Done, please upvote me back!"

    similar_words = d.suggest(word)
    for similar in similar_words:
        reply_text += similar + " "


    comment.reply(reply_text)
