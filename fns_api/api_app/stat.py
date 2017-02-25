from datetime import datetime, date


class Stat():

    def __init__(self, date_from, date_to, length):
        DP = "%Y-%M-%d"

        self.date_from = datetime.strptime(DP, date_from).date()
        self.date_to = datetime.strptime(DP, date_to).date()
        self.length = length

        self.stat_list = []


class NewsProvider():

    def __init__(self, name):
        self.name = name
        self.count = 0
        self.link = []

    def add_count(d=1)
        self.count += d

    def append_link(link_obj)
        self.link.append(link_obj)


class Portal(NewsProvider):

    def __init__(self, name, hostname):
        NewsProvider.__init__(name)
        self.hostname = hostname


class Page(NewsProvider):

    def __init__(self, name, pid):
        NewsProvider__init__(name)
        self.pid = pid

        self.type_link = 0
        self.type_video = 0
        self.type_none_or_photo = 0


class Link():

    def __init__(self, title, description, image, url):
        self.title = title
        self.description = description
        self.image = image
        self.url = url
        self.count = count

    def add_count(d=1)
        self.count += d
