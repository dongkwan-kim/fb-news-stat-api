import re
import pprint
from collections import defaultdict


def log_parse(log, stat_type):
    """
    @param log TYPE DICT
    @param stat_type TYPE STRING
    """

    if stat_type == "portal":
        return parse_portal(log)

    elif stat_type == "page":
        pass

re_portal = {
    "naver": "^http.*news\.naver\.com",
    "daum": "^http.*media\.daum\.net",
    "nate": "^http.*news\.nate\.com",
    "zum": "^http.*news\.zum\.com|^http.*m\.zum\.com/news",
    "msn": "^http.*msn\.com/ko-kr/news|^http.*msn\.com/ko-kr/.+/news"
}

pa_portal = { name:re.compile(regex) for (name, regex) in re_portal.items() }

def parse_portal(log):
    portal_dict = defaultdict(list)
    for a in collect_tag(log, "a"):
        for name, pattern in pa_portal.items():
            if pattern.search(a):
                portal_dict[name].append(a)
    return portal_dict

def parse_page(log):
    raise NotImplementedError

def collect_tag(log, tag):
    """
    @param log TYPE DICT
    @param tag TYPE STRING
    @param TYPE LIST: list of tag_value
    """
    r_list = []
    tag_list = log.keys()
    if tag in tag_list:
        r_list.append(log[tag])
    if "article" in tag_list:
        for article in log["article"]:
            r_list += collect_tag(article, tag)
    return r_list


