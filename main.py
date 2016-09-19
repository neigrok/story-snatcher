import storyClass
import parsev2
import os

storyClass.Story.initstories(parsev2.collectworks())
if not os.path.exists('Stories/'):
    os.makedirs('Stories/')
for story in storyClass.Story.stories:
        f = open('Stories/' + story.getheader() + ".txt", mode="w", encoding="UTF-8")
        f.write(story.getbody())
        f.flush()
        f.close()
