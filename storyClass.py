class Story:
    """Class for stories. Each story has header + body parsed from html"""

    global stories

    def __init__(self, header=None, body=None):
        formatted = header.replace("\"", "\'")  # replace for windows
        formatted = formatted.replace("?", "777")  # replace for windows
        formatted = formatted.replace("*", "")  # replace for windows
        self.header = formatted
        self.body = body

    def getheader(self):
        return self.header

    def getbody(self):
        return self.body

    @staticmethod
    def initstories(dict):
        Story.stories = list()
        for item in dict:
            Story.stories.append(Story(header=item, body=dict.get(item)))
