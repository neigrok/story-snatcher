from ver2 import storyClass
from ver2 import parsev2

storyClass.Story.initstories(parsev2.collectworks(16))
#f = open("/Stories/::num", mode="r")
#num = int(f.readline())
#f.close()

for story in storyClass.Story.stories:
    #f = open("Stories/" + str(num) + story.getheader(), mode="w")
    f = open("Stories/" + story.getheader(), mode="w")
    f.write(story.getbody())
    f.flush()
    f.close()
    #num += 1

#f = open("/Stories/::num", mode="w")
#f.write(num)
#f.flush()
#f.close()