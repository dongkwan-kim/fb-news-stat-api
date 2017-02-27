from datetime import datetime, date
from api_app.log_parse import log_parse

class Stat():

    def __init__(self, date_from, date_to, length, stat_type):
        DP = "%Y-%m-%d"

        self.date_from = datetime.strptime(date_from, DP).date()
        self.date_to = datetime.strptime(date_to, DP).date()
        self.length = length

        self.stat_type = stat_type
        self.stat_list = []

    def append(self, stat):
        self.stat_list.append(stat)

    def dump(self):
        return [s.dump() for s in self.stat_list]

    def is_valid_log(self, enc_log):
        lv = enc_log.last_visit
        if self.date_from <= lv and lv <= self.date_to:
            return True
        else:
            return False

    def update(self, enc_log):
        """
        enc_id = models.CharField(max_length=64)
        enc_info = models.TextField()
        last_visit = models.DateField()
        """
        if not self.is_valid_log(enc_log):
            return False

        for log in json.dumps(enc_log.enc_info):
            parse_result = log_parse(log)




class NewsProvider():

    def __init__(self, name):
        self.name = name
        self.count = 0
        self.link = []

    def add_count(self, d=1):
        self.count += d

    def append_link(self, link_obj):
        self.link.append(link_obj)

    def dump(self):
        d = vars(self)
        d["link"] = [l.dump() for l in self.link]
        return d


class Portal(NewsProvider):

    def __init__(self, name, hostname):
        NewsProvider.__init__(self, name)
        self.hostname = hostname


class Page(NewsProvider):

    def __init__(self, name, pid):
        NewsProvider.__init__(self, name)
        self.pid = pid
        self.ptype = PageType()

    def dump(self):
        d = NewsProvider.dump(self)
        d["ptype"] = self.ptype.dump()
        return d


class PageType():

    def __init__(self):
        self.link = 0
        self.video = 0
        self.none_or_photo = 0

    def dump(self):
        return vars(self)


class Link():

    def __init__(self, title, description, image, url):
        self.title = title
        self.description = description
        self.image = image
        self.url = url
        self.count = 0

    def add_count(self, d=1):
        self.count += d

    def dump(self):
        return vars(self)


if __name__ == "__main__":
    import pprint
    l_1 = Link("ti1", "des1", "img1", "url1")
    l_2 = Link("ti2", "des2", "img2", "url2")
    l_3 = Link("ti3", "des3", "img3", "url3")

    p_1 = Portal("p1", "p1_id")
    p_1.append_link(l_1)
    p_1.append_link(l_2)

    p_2 = Portal("p2", "p2_id")
    p_2.append_link(l_3)

    s = Stat("2017-02-15", "2017-02-20", 10)
    s.append(p_1)
    s.append(p_2)

    pprint.pprint(s.dump())
