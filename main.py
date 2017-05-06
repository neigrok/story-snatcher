from story_snatcher.getHTML import getHTML
from story_snatcher.parse import parse, write

if __name__ == '__main__':
    html = getHTML()
    stories = parse(html)
    write('stories.csv', stories)