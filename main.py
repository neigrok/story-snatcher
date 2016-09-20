import storyClass
import os
from ver3 import parseV3

stories = parseV3.collectworks()
storyClass.Story.initstories(dict=stories)
if not os.path.exists('Stories/'):
    os.makedirs('Stories/')
for story in storyClass.Story.stories:
        f = open('Stories/' + story.getheader() + ".txt", mode="w", encoding="UTF-8")
        f.write(story.getbody())
        f.flush()
        f.close()
