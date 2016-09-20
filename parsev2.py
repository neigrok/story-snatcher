from bs4 import BeautifulSoup
import getHTML


def makefiles(daysago=-1):
    html = getHTML.getHTML(daysago)
    soup = BeautifulSoup(html, 'html.parser')

    headers = soup.find_all("div", {"class": "story__header-title"})
    stories = soup.find_all("div", {"class": "b-story__content b-story__content_type_text"})

    h = open("headers.txt", mode="w", encoding="UTF-8")
    s = open("stories1.txt", mode="w", encoding="UTF-8")

    for header in headers:
        h.write(str(header))
        print(header)

    for story in stories:
        s.write(str(story))

    h.close()
    s.close()


def cleanheaders():

    h = open("headers.txt", mode="r", encoding="UTF-8")
    lines = h.readlines()
    h.close()
    h = open("headers.txt", mode="w", encoding="UTF-8")
    headers = ''.join(lines)
    for header in headers.split("</a>"):
        if "_blank\"" in header:
            h.write(header[header.find("_blank\"")+len("_blank\""):] + '\n')
    h.close()


def cleanstories():

    s = open("stories1.txt", mode="r", encoding="UTF-8")
    lines = s.readlines()
    s.close()
    s = open("stories1.txt", mode="w", encoding="UTF-8")
    headers = ''.join(lines)
    for header in headers.split("</div>"):
        if "data-expanded=\"1\"" in header:
            s.write(header[header.find("data-expanded=\"1\"")+len("data-expanded=\"1\""):] + '\n')
    s.close()


def removetags():

    s = open("stories1.txt", mode="r", encoding="UTF-8")
    lines = s.readlines()
    s.close()
    s = open("stories1.txt", mode="w", encoding="UTF-8")
    for line in lines:
        soup = BeautifulSoup(line, 'html.parser')
        links = soup.findAll('noindex')

        for link in links: #clean links (href)
            line = line.replace(str(link), "")

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


def collectworks(daysago =- 1):

    makefiles(daysago)
    cleanheaders()
    cleanstories()
    removetags()

    h = open("headers.txt", mode="r", encoding="UTF-8")
    lines = h.readlines()
    h.close()

    headers = ''.join(lines)
    headersarr = [header.replace('\n', '') for header in headers.split(">") if header != '']

    s = open("stories1.txt", mode="r", encoding="UTF-8")
    lines = s.readlines()
    s.close()

    stories = ''.join(lines)
    storiesarr = [story.replace('\t', '') for story in stories.split(">") if story != '']

    return dict(zip(headersarr, storiesarr))
