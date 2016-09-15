import sys
from bs4 import BeautifulSoup

def parseTaggedStories(html):
    f = open("Snatch", mode="w")
    sys.stdout = f
    soup = BeautifulSoup(html, 'html.parser')
    stories = soup.find_all("div", {"class":"b-story__content b-story__content_type_text"})
    for story in stories:
        print(story, end="\n\n")
    f.close()
    sys.stdout = sys.__stdout__

def removeTags():
    f = open("Snatch", mode="r")
    lines = f.readlines()
    f.close()

    f = open("Snatch", mode="w")
    for line in lines:
        if line != '''<div class="b-story__content b-story__content_type_text" data-expanded="1">''' + "\n"\
                and line != '</div>' + "\n":
            line = line.replace("</p><p><br/></p><p>", "\n")
            line = line.replace("</p><p>", "\n")
            line = line.replace("<br/>", "")
            f.write(line)
    f.close()

def sortbyfiles():
    f = open("Snatch", mode="r")
    lines = f.readlines()
    f.close()
    i = 0
    stories1 = ''.join(lines)
    for paragraphs in stories1.split("</p>"):
        if "<p>" in paragraphs:
            f = open("stry"+str(i),mode="w")
            f.write(paragraphs[paragraphs.find("<p>")+len("<p>"):])
            f.flush()
            f.close()
            i += 1
