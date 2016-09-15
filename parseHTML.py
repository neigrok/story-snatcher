from bs4 import BeautifulSoup
import getHTML
import sys

# сначала заменить </p><p><br/></p><p> на \n
# потом заменить </p><p> на \n



#def parseTaggedStories():
f = open("Snatch", mode="w")
sys.stdout = f
soup = BeautifulSoup(getHTML.getHTML(), 'html.parser')
stories = soup.find_all("div", {"class":"b-story__content b-story__content_type_text"})
for story in stories:
    print(story, end="\n\n")
f.close()
sys.stdout = sys.__stdout__

#def removeTags():
f = open("Snatch", mode="r")
lines = f.readlines()
for line in lines:
    line = line.replace("</p><p>", "\n")
f.close()
f = open("Snatch", mode="w")
for line in lines:
    if line != '''<div class="b-story__content b-story__content_type_text" data-expanded="1">''' + "\n"\
            and line != '</div>' + "\n":
        f.write(line)
f.close()