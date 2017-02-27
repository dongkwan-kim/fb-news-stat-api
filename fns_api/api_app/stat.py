import json
from datetime import datetime, date
from api_app.log_parse import log_parse
from api_app.news_meta import get_og_meta
import hashlib
import random

class Stat():

    def __init__(self, date_from, date_to, length, stat_type):
        DP = "%Y-%m-%d"

        self.date_from = datetime.strptime(date_from, DP).date()
        self.date_to = datetime.strptime(date_to, DP).date()
        self.length = int(length)
        if self.length > 20:
            self.length = 20

        self.stat_type = stat_type
        self.stat_list = []

    def append(self, stat):
        self.stat_list.append(stat)

    def dump(self):
        return [s.dump(self.length) for s in self.stat_list]

    def is_valid_log(self, enc_log):
        lv = enc_log.saved_date
        if self.date_from <= lv and lv <= self.date_to:
            return True
        else:
            return False

    def update(self, enc_log):
        """
        enc_id = models.CharField(max_length=64)
        enc_info = models.TextField()
        saved_date = models.DateField()
        """
        if not self.is_valid_log(enc_log):
            return False

        for log in json.loads(enc_log.enc_info):
            parse_result = log_parse(log, self.stat_type)

            if self.stat_type == "portal":
                self.update_portal(parse_result)

            elif self.stat_type == "page":
                pass

    def update_portal(self, parse_result):
        # defaultdict(list), key: portal, value: [url]
        for p_name, url_list in parse_result.items():
            new_portal = Portal(p_name, p_name)
            for url in url_list:
                new_link = Link(url)
                new_portal.append_link(new_link)

            if new_portal in self.stat_list:
                idx = self.stat_list.index(new_portal)
                self.stat_list[idx] += new_portal
            else:
                self.append(new_portal)


class NewsProvider():

    def __init__(self, name):
        self.name = name
        self.count = 0
        self.link = []

    def add_count(self, d=1):
        self.count += d

    def append_link(self, link_obj):
        if link_obj in self.link:
            idx = self.link.index(link_obj)
            self.link[idx] += link_obj

        else:
            self.link.append(link_obj)

        self.add_count(link_obj.count)

    def dump(self, length):
        d = vars(self)

        link_list = sorted(self.link, reverse=True, key=lambda x: x.count)[:length]
        for l in link_list:
            l.meta()
        d["link"] = [l.dump() for l in link_list]

        return d

    def __add__(self, other):
        for o_link in other.link:
            self.append_link(o_link)
        return self

class Portal(NewsProvider):

    def __init__(self, name, hostname):
        NewsProvider.__init__(self, name)
        self.hostname = hostname

    def __eq__(self, other):
        try:
            return self.hostname == other.hostname
        except:
            return False


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

    def __init__(self, url):
        self.title = ""
        self.description = ""
        self.image = ""
        self.url = url
        self.count = 1
        self.lid = hashlib.sha224(str(random.random()).encode("utf-8")).hexdigest()

    def add_count(self, d=1):
        self.count += d

    def meta(self):
        try:
            meta_dict = get_og_meta(self.url)
            self.title = meta_dict["title"]
            self.description = meta_dict["description"]
            self.image = meta_dict["image"]
            self.url = meta_dict["url"]
        except:
            pass

    def dump(self):
        return vars(self)

    def __eq__(self, other):
        return self.url == other.url

    def __add__(self, other):
        sum_count = self.count + other.count
        self.count = sum_count
        return self


if __name__ == "__main__":
    import pprint
    l_1 = Link("url1")
    l_2 = Link("url1")
    l_3 = Link("url3")

    l_t = l_1 + l_2
    print(l_t.count)
