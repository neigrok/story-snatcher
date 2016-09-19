class Story:

    """Class for stories. Each story has header + body parsed from dictionary"""

    global stories

    def __init__(self, header=None, body=None):
        self.header = header.replace("\"", "\'") #replace for windows
        self.body = body

    def getheader(self):
        return self.header

    def getbody(self):
        return self.body

    def initstories(dic):
        Story.stories = list()
        for item in dic:
            Story.stories.append(Story(header=item, body=dic.get(item)))
