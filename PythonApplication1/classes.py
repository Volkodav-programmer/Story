class Part:
    def __init__(self, number, content):
        self.number = number
        self.content = content
        self.next_part = None

    def read(self):
        return self.content

    def __str__(self):
        return "Part Nr " + str(self.number)

    def __repr__(self):
        return str(self.number)
