# Simple-Reddit-Scraper
A simple reddit images scraper written with [PRAW](https://praw.readthedocs.io/en/latest/) (The Python Reddit API Wrapper).

# Description
This script downloads the top images from a list of subreddits provided in a text file and downloads the images into a subdirectory named after the subreddit's name.

Note that this program was written as a part of a  university project I had. Hence, this program will not be maintaned and could possibly  have issues

 # Usage 
 - Make sure you have [PRAW](https://praw.readthedocs.io/en/latest/) installed. To install
   using `pip` simply type in your terminal:
   
       pip install praw
 - Replace the `client_id` and `client_secret` in the code with your own. Obtain your own [here](https://www.reddit.com/prefs/apps/) and refer to the reddit APIs documentation for further assistance.
 - Type in `python SimplePythonScraper.py --help`  in your terminal to check usage.

>     usage: SimplePythonScraper.py [-h] -r [subreddits list]
>                                   [-d [destination folder]] [-n [number of posts]]
>                                   [-s]
>     
>     optional arguments:
>       -h, --help            show this help message and exit
>       -r [subreddits list], --subreddits [subreddits list]
>                             specify a text file containing list of subreddits.
>       -d [destination folder], --dest [destination folder]
>                             specify directory for saving the images (default =
>                             current directory).
>       -n [number of posts], --num_posts [number of posts]
>                             specify number of posts to check (default = 50).
>       -s, --sfw             add this to only download SFW posts.


