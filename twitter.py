from __future__ import print_function
import os
import tweepy #use pip install tweepy in terminal

try:
    input = raw_input
except NameError:
    pass


def getStatus():
    lines = []
    while True:
        line = input()
        if line:
            lines.append(line)
        else:
            break
    status = '\n'.join(lines)
    return status

def tweetthis(type):
	if type == "text":
		print("Enter your tweet "+user.name)
		tweet = getStatus()
		try:
			api.update_status(tweet)
		except Exception as e:
			print(e)
			return
    elif type == "pic":
	#make sure that the path is in the folder of this file or a folder in the folder.
	#Example: if you have this on your desktop and the pic is also on your desktop then just put the pic name with the extension (example.png)
	#if its in a folder on your desktop then put the path as the folder name / pic name with extansion (examplepic/example.png)
		print("Enter pic path "+user.name)
		pic = os.path.abspath(input())
		print("Enter status "+user.name)
		title = getStatus()
		try:
			api.update_with_media(pic, status=title)
		except Exception as e:
			print(e)
			return

	print("\n\nDONE!!")

def initialize():
    #Create a twitter app "apps.twitter.com" to get your OAuth requirements.
	global api, auth, user
	ck = "here" # consumer key
	cks = "here" # consumer key SECRET
	at = "here" # access token
	ats = "here" # access token SECRET

	auth = tweepy.OAuthHandler(ck,cks)
	auth.set_access_token(at,ats)

	api = tweepy.API(auth)
	user = api.me()

def main():
	doit = int(input("\n1. text\n2. picture\n"))
	initialize()
	if doit == 1:
		tweetthis("text")
	elif doit == 2:
		tweetthis("pic")
	else:
		print("OK, Let's try again!")
		main()

main()
