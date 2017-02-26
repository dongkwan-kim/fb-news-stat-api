from api_app.stat import Link
import urllib.request
import urllib.parse
import re


def get_og_meta(news_link):
    """
    @param news_link TYPE URL
    @return TYPE Link(title, description, image, url)
    """

    title = ''
    description = ''
    image = ''
    url = ''
    request = urllib.request.Request(
        news_link, headers={'User-Agent': 'Mozilla/5.0'})
    response = urllib.request.urlopen(request)
    for line in response:
        line = line.decode("utf-8")
        matchObj = re.match(
            r'.*[\'\"]og:(\w*)[\'\"].*content.*[\'\"](.*)[\'\"].*', line, re.M | re.I)
        if matchObj:
            tagType = matchObj.group(1)
            if tagType == 'title':
                title = matchObj.group(2)
            elif tagType == 'description':
                description = matchObj.group(2)
            elif tagType == 'image':
                image = matchObj.group(2)
            elif tagType == 'url':
                url = matchObj.group(2)

    return Link(title, description, image, url)