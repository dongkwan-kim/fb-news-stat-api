import re


def log_parse(log, stat_type):
    """
    @param log TYPE DICT
    @param stat_type TYPE STRING
    """

    if stat_type == "portal":
        return parse_portal(log)

    elif stat_type == "page":
        pass

def parse_portal(log):
    for a in collect_tag(log, "a"):
        //TODO
        pass

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


