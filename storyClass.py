class Story:
    def __init__(self, title, text):
        self.title = title
        self.text = text

    def __str__(self):
        return self.title