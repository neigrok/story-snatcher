from bs4 import BeautifulSoup
import getHTML
import re


def collectworks(daysago=-1):

    #request
    html = getHTML.getHTML(daysago)
    soup = BeautifulSoup(html, 'html.parser')

    #get
    stories = soup.find_all("div", {"class": "story"})
    #create dict
    storycollection = dict()

    #refine stories
    for story in stories:
        try:
            header = re.findall(r'blank">(.*?)<', str(story))[0]
        except IndexError:
            continue

        soup = BeautifulSoup(str(story), 'html.parser')
        text = soup.find_all("div", {"class": "b-story-block__content"})
        if str(text) == "[]":
            text = soup.find_all("div", {"class": "b-story__content b-story__content_type_text"})

        soup = BeautifulSoup(str(text), 'html.parser')
        links = soup.findAll('noindex')

        # clean links (href)
        for link in links:
            text = str(text).replace(str(link), "")
        #clean tags
        text = str(text).replace("</p><p><br/></p><p>", "\n")
        text = text.replace("</p><p>", "\n")
        text = text.replace("<br/>", "")
        text = text.replace(">\n<p>", ">")
        text = text.replace("<p>", "")
        text = text.replace("</p>", "")
        text = text.replace("<br>", "")
        text = text.replace("</br>", "")
        text = text.replace("</br>", "")
        text = text.replace("<i>", "")
        text = text.replace("</i>", "")
        text = text.replace("</div>", "")
        text = text.replace("<div class=\"b-story__content b-story__content_type_text\" data-expanded=\"1\">", "")
        text = text.replace("<div class=\"b-story-block__content\">", "")

        if "img alt" in text or text == "[]":
            continue

        storycollection[header] = text

    return storycollection

