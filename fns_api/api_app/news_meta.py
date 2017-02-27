import urllib.request
import urllib.parse
import re

def get_og_meta(news_link, is_naver=False):
    """
    @param news_link TYPE URL
    @return TYPE DICT {title, description, image, url}
    """
    naver_p = re.compile("^http://news.naver.com")
    if naver_p.match(news_link):
        news_link = m_naver(news_link)

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
            r'.*[\'\"]og:(\w*)[\'\"].*content.*[\"](.*)[\"].*', line, re.M | re.I)
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

    r = {
        "title": html_decode(title),
        "description": html_decode(description),
        "image": image,
        "url": url,
    }
    return r

def m_naver(naver_link):
    naver_link = naver_link.replace("main/read.nhn", "read.nhn")
    naver_link = naver_link.replace("news.naver.com", "m.news.naver.com")
    return naver_link

def html_decode(s):
    htmlCodes = (
            ("'", '&#39;'),
            ('"', '&quot;'),
            ('>', '&gt;'),
            ('<', '&lt;'),
            ('&', '&amp;')
        )
    for code in htmlCodes:
        s = s.replace(code[1], code[0])
    return s

if __name__ == "__main__":
    url = "http://news.naver.com/main/read.nhn?mode=LSD&mid=sec&sid1=102&oid=032&aid=0002766273"
    l = get_og_meta(url, True)
    print(l)

