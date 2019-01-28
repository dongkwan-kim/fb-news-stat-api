# fb-news-stat-api
- Joint project for google newslab fellowship 16/17

## Deprecation notice
- Since March 14 2017

## Description
Unlike the first Google Newslab Fellowship, during which the subject of the common project was
set as 'surveillance', the second fellowship did not have a subject, so the hackerthon on January 25th
was organized to select the best idea as the subject. 17 fellows, excluding the developers were divided
into four groups and participated in the hackerthon about 'data journalism' 'crowdsourcing journalism'
from 14:00 to 18:30. The three developers gave technical advice when the teams asked. Ideas such as
'the difficulty of the driving license test and the number of car accidents', 'Seoul Safe return map',
'Real time/location based fine dust information service', and 'Visualization of connection between the
press freedom index and press-related issues' etc. were gathered during the hackerthon. The judges,
made up of developers and coordinators, assessed the groups with criteria like 'level of fun',
‘realizability’, and 'design quality' etc. The 'Seoul Safe Return map' received the highest grade.

The 'Seoul safe return map' was not made because a prominent service already exists. [Korea Safety
Map](http://www.safemap.go.kr/) is a website managed by the National Disaster Management
Research Institute. In addition to safety-related issues such as sexual violence, robbery, violence etc.
this site supports disaster safety and transport safety. This website was considered more superb than
the 'Seoul safe return map' because it offers visualization of the distance level for the entire country.
All the coordinators agreed that trying a different project would be better than proceeding with a
project that is worse than an existing service.

The actual common project that was produced was 'API statistics of Facebook News consumption'
and using this, the 'Facebook news consumption statistics dashboard' This API was based on the
database of Team O-Right, the team that cooperated with Joong Ang Ilbo during the second Google
Newslab fellowship.

The database in question stores the page name, representative link, time etc. that is posted on
Facebook. Using this, the way news is consumed through Facebook can be checked. The information
that the API provides is the following. (1) Page name, page link, the frequency of page appearance,
57
representative link, the frequency of link appearance, frequency of video/link appearance, for the
news that is provided by the page. (2) Portal name, portal address, frequency of portal appearance,
link, frequency of link appearance about the news provided by portals (Naver, Daum, Nate, Zum,
MSN). (3) Demographic information of users. To use the API, you have to be given the access token.
Currently two tokens have been issued. In the future an automatized token application and provision
process will be supported. Also, the personal information of the database will be encrypted (SHA-2),
so the specific user cannot be discerned.

[The Facebook News consumption statistics dashboard](https://github.com/dongkwan-kim/fb-news-stat-api#project-example)
uses the above API to visualize statistics of Facebook news consumption. The statistical graph, the
ranking of the links consumed during a specified period, the ranking of page consumption, the ranking
of portal consumption etc. are shown.

## Database
- From team O'Right (Google News Lab Fellowship 16/17)

## API

### Convention
- token: user's own token
- DATE: r'^[0-9]{4}-[0-9]{2}-[0-9]{2}$' or Empty string

### API Endpoints
- URL: https://fnsapi.newslabfellows.com/api/v1

### Token
- You need to get your own token to use this api.
- Token registration is not supported yet.
- You can use test token

### Statistics
- GET /portal/
- parameter
  - date_from TYPE DATE
  - date_to TYPE DATE
  - token TYPE SHA-224-STRING
  - length TYPE INT
- result TYPE JSON

```javascript
[
  {
    "name": (TYPE STRING),
    "hostname": (TYPE STRING),
    "count": (TYPE INT),
    "link": [
      {
        "title": (TYPE STRING),
        "description": (TYPE STRING),
        "image": (TYPE URL),
        "url": (TYPE URL),
        "count": (TYPE INT),
      },
    ]
  },
]
```
- GET /page/
- parameter
  - date_from TYPE DATE
  - date_to TYPE DATE
  - token TYPE SHA-224-STRING
  - length TYPE INT
- result TYPE JSON

```javascript
[
  {
    "name": (TYPE STRING),
    "pid": (TYPE STRING),
    "count": (TYPE INT),
    "link": [
      {
        "title": (TYPE STRING),
        "description": (TYPE STRING),
        "image": (TYPE URL),
        "url": (TYPE URL),
        "count": (TYPE INT),
      },
    ],
    "ptype": {
      "link": (TYPE INT),
      "video": (TYPE INT),
      "none_or_photo": (TYPE INT),
    }
  }
]
```

## Project Example
- https://fnsapi.newslabfellows.com/fbnews
![example image](https://raw.githubusercontent.com/dongkwan-kim/fb-news-stat-api/master/gnl_1617_fb-news-api.jpg)

## [Presentation](https://github.com/dongkwan-kim/fb-news-stat-api/blob/master/gnl_1617_fb-news-api.pdf)
- Graduation ceremony at gnl 16/17 (2017.02.28)

## Developers
- [@dongkwan-kim](https://github.com/dongkwan-kim)
- [@Jiwoopark0508](https://github.com/Jiwoopark0508)
- [@juhojuho](https://github.com/juhojuho)
