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

    k_encode = ["euc-kr", "utf-8"]
    charset = k_encode.pop()

    for line in response:
        try:
            line.decode(charset)
        except:
            charset = k_encode.pop()

        line = line.decode(charset)

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

        if title and description and image and url:
            break

    return Link(title, description, image, url)

if __name__ == "__main__":
    url_1 = "http://news.chosun.com/site/data/html_dir/2017/02/26/2017022601574.html?Dep0=facebook&topics"
    url_2 = "http://news.joins.com/article/21312373?cloc=joongang%7Csns%7Cfb"
    l = get_og_meta(url_1)
    print(l.dump())

