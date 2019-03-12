# 	====== Written by KaramMTayyem ======	

import praw
import argparse
import sys
import re
import os
from urllib.request import urlopen



#================================================================================================#
# 	Method scrape_list is responsible for traversing through the subreddit list. It creates a
#	a new folder for each subreddit, then calls a method to start scraping the given subreddit
#================================================================================================#
def scrape_list(list_name, directory_to_save, number, only_sfw):
	with open(list_name) as sublist:
		for sub in sublist:
			sub_directory = os.path.join(directory_to_save, sub.strip())
			if not os.path.exists(sub_directory):
				os.makedirs(sub_directory)
			scrape_subreddit(sub.strip(), number, sub_directory, only_sfw)



#================================================================================================#
# 	Method scrape_subreddit is responsible for scraping an individual subreddit. It creates a new
#	instance of the subreddit, then traverses through the top posts of all time. For each posts,
#	it checks whether it is a picture or not and checks whether it is NSFW depending. It then
#	downloads the image to the subdirectory named after the subreddit.
#================================================================================================#
def scrape_subreddit(subreddit_name, number_of_posts, sub_directory, only_sfw):
	c = 0
	if(number_of_posts > 1000):
		print("[WARNING] Reddit limits the number of each listing to 1000.")
	subreddit = reddit.subreddit(subreddit_name)
	if(subreddit.over18 and only_sfw):
		print("[WARNING]", subreddit_name, "is an NSFW subreddit. Skipping...")
		return
	for submission in subreddit.top('all', limit=None):
		if(is_picture(submission.url)):
			if(submission.over_18 and only_sfw):
				continue
			download_image(submission.url, str(c)+".jpg", sub_directory)
			print("[*] Downloaded", submission.url)
			c+=1
			if(c >= number_of_posts):
				return



#================================================================================================#
# 	Method is_picture checks whether a given URL is a URL of an image judging by file extension.
#================================================================================================#
def is_picture(url):
	if re.search(r'https?:.*\.(jpg|jpeg|png)', url, flags=re.IGNORECASE) is None:
		return False;
	return True;



#================================================================================================#
# 	Method download_image downloads image file from a given URL.
#================================================================================================#
def download_image(url, filename, directory):
	try:
		imagedata = urlopen(url).read()
		with open(os.path.join(directory,filename), mode='wb') as imagefile:
			imagefile.write(imagedata)
	except:
		print("[ERROR] Failed to download", url)
		return




#================================================================================================#
#	Creating a Reddit instance to use the API	
#	YOU MUST INSERT YOUR client_id, client_secret here
#================================================================================================#
reddit = praw.Reddit(client_id='<YOUR_CLIENT_ID>',
                     client_secret='<YOUR_CLIENT_SECRET>',
                     user_agent='Python:SimpleRedditScraper:1.0 (by KTayyem)')


#================================================================================================#
# 			Default is to download posts regardless of whether they are SFW or not.
#		This value gets changed into true when users execute with the argument -s or --sfw
#================================================================================================#
is_sfw = False


#================================================================================================#
# 	The following lines prepare the argument parser responsible for parsing the arguments	
# given through the command line. They configure the parser and how each value should be assigned.
#================================================================================================#
parser = argparse.ArgumentParser()
parser.add_argument('-r', '--subreddits',
 	nargs='?', metavar='subreddits list',
 	help = "specify a text file containing list of subreddits.",
 	required=True)
parser.add_argument('-d', '--dest', 
	nargs='?', 
	metavar='destination folder', 
	help='specify directory for saving the images (default = current directory).', 
	default='.')
parser.add_argument('-n', '--num_posts', 
	nargs='?', 
	metavar='number of posts', 
	type=int, 
	help='specify number of posts to check (default = 50).', 
	default=50)
parser.add_argument('-s', '--sfw', 
	help='add this to only download SFW posts.',
	action='store_true')
args = parser.parse_args()

#================================================================================================#
# 	The method call that starts it all!	
#================================================================================================#
scrape_list(args.subreddits, args.dest, args.num_posts, args.sfw)


	


