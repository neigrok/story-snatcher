import storyClass
import parsev2

storyClass.Story.initstories(parsev2.collectworks())

for story in storyClass.Story.stories:
        f = open('Stories/' + story.getheader() + ".txt", mode="w", encoding="UTF-8")
        f.write(story.getbody())
        f.flush()
        f.close()
