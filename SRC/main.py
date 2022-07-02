import praw
import pandas as pd

reddit = praw.Reddit(client_id="Ap5V7_AFJEFZsL9VI8vj1w",  # your client id
					 client_secret="R24dIQz0LHNe6AxAWmJAuq98m3bMqg",  # your client secret id
					 user_agent='TestingWebScrape')  # your user agent (can be anything)

# subreddit = reddit.subreddit("Wallpaperland") # name of subreddit

# # Display the name of the Subreddit
# print("Display Name:", subreddit.display_name)
#
# # Display the title of the Subreddit
# print("Title:", subreddit.title)
#
# # Display the description of the Subreddit
# print("Description:", subreddit.description)
# print()
#
# for post in subreddit.hot(limit=3):
#     print("Post: ", post.title)
	####################################################################################################

posts = []
wp = reddit.subreddit('Wallpaperland')
for post in wp.hot(limit=5):
    posts.append([post.title, post.score, post.id, post.subreddit, post.url])

posts = pd.DataFrame(posts,columns=['title', 'score', 'id', 'subreddit', 'url'])

print(posts)


submission = reddit.submission("vhdjpf")
for top_level_comment in submission.comments:
    print("Comment: ")
    print(top_level_comment.body)