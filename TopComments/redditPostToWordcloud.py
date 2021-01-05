import praw
from wordcloud import WordCloud, STOPWORDS
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

thread = ""  # Enter the ID you wish to scrape


common = open("google-10000-english.txt", 'r')
for line in common:

    # reading each word
    for word in line.split():

        # displaying the words
        STOPWORDS.add(word)


stop_words = set(STOPWORDS)
content = ''

reddit = praw.Reddit(
    user_agent="",
    client_id="Enter your id",
    client_secret="Enter your client secret",
    username="Enter your username",
    password="Enter your password"
)


submission = reddit.submission(id=thread)


a = list()
try:
    for top_level_comment in submission.comments:
        a.append(top_level_comment.body)

except:
    print("done")
t = list()
for i in a:
    t.append(i.split())
print(t)


for x in t:
    content += " ".join(x)+" "
print(content)

image_mask = np.array(Image.open("mask-circle.png"))
wc = WordCloud(background_color="white", max_words=900,
               width=4000, height=2400, scale=10, mask=image_mask)
wc.generate(content)
plt.imshow(wc)
wc.to_file("word_cloud.png")
