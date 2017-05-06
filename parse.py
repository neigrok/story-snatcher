from bs4 import BeautifulSoup
from story_snatcher.storyClass import Story
import csv


def parse(html):
    soup = BeautifulSoup(html, "html.parser")
    stories = []
    soupstories = soup.find_all(class_='story')

    for story in soupstories:
        if story.get('data-story-long', 'true') == 'true':
            continue

        title = story.find(class_='story__title-link').text
        try:
            text = story.find(class_='b-story__content b-story__content_type_text').text
        except AttributeError:
            print('%s - картинка' % title)
        else:
            stories.append(Story(title, text))

    return stories


def write(path, stories):
    with open(path, 'w', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        for story in stories:
            writer.writerow((story.title, story.text))