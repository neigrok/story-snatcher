from bs4 import BeautifulSoup

from ver2 import getHTML


def makefiles(daysago=-1):
    html = getHTML.getHTML(daysago)
    soup = BeautifulSoup(html, 'html.parser')

    headers = soup.find_all("div", {"class": "story__header-title"})
    stories = soup.find_all("div", {"class": "b-story__content b-story__content_type_text"})

    h = open("headers", mode="w")
    s = open("stories", mode="w")

    for header in headers:
       h.write(str(header))

    for story in stories:
       s.write(str(story))

    h.close()
    s.close()

def cleanheaders():

    h = open("headers", mode="r")
    lines = h.readlines()
    h.close()
    h = open("headers", mode="w")
    headers = ''.join(lines)
    for header in headers.split("</a>"):
       if "_blank\"" in header:
           h.write(header[header.find("_blank\"")+len("_blank\""):] + '\n')
    h.close()

def cleanstories():

    s = open("stories", mode="r")
    lines = s.readlines()
    s.close()
    s = open("stories", mode="w")
    headers = ''.join(lines)
    for header in headers.split("</div>"):
        if "data-expanded=\"1\"" in header:
            s.write(header[header.find("data-expanded=\"1\"")+len("data-expanded=\"1\""):] + '\n')
    s.close()

def removetags():

    s = open("stories", mode="r")
    lines = s.readlines()
    s.close()

    s = open("stories", mode="w")
    for line in lines:
         line = line.replace("</p><p><br/></p><p>", "\n")
         line = line.replace("</p><p>", "\n")
         line = line.replace("<br/>", "")
         line = line.replace(">\n<p>", ">")
         line = line.replace("<p>", "")
         line = line.replace("</p>", "")
         line = line.replace("<br>", "")
         line = line.replace("</br>", "")
         line = line.replace("</br>", "")
         line = line.replace("<i>", "")
         line = line.replace("</i>", "")
         s.write(line)
    s.close()

def collectworks(daysago=-1):

    makefiles(daysago)
    cleanheaders()
    cleanstories()
    removetags()

    h = open("headers", mode="r")
    lines = h.readlines()
    h.close()

    headers = ''.join(lines)
    headersarr = [header.replace('\n', '') for header in headers.split(">") if header != '']

    s = open("stories", mode="r")
    lines = s.readlines()
    s.close()

    stories = ''.join(lines)
    storiesarr = [story.replace('\t', '') for story in stories.split(">") if story != '']

    return dict(zip(headersarr, storiesarr))
