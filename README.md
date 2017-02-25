# fb-news-stat-api
Joint project for google newslab fellowship 16/17

## Database

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
- GET /stats/
- parameter
  - date_from TYPE DATE
  - date_to TYPE DATE
  - token TYPE SHA-224-STRING
- result TYPE JSON

```javascript
{
  "portal": {
    "host": [
      {
        "name": (TYPE STRING),
        "hostname": (TYPE STRING),
        "count": (TYPE INT),
      },
    ],
    "link": [
      {
        "link": (TYPE URL),
        "count": (TYPE INT),
      },
    ]
  },
  "page": {
    "host": [
      {
        "name": (TYPE STRING),
        "id": (TYPE STRING),
        "count": (TYPE INT),
      },
    ],
    "link": [
      {
        "link": (TYPE URL),
        "count": (TYPE INT),
      },
    ],
    "type": {
      "link": (TYPE INT),
      "video": (TYPE INT),
      "none_or_photo": (TYPE INT),
    }
  },
  "user": {
    "gender": [
      {
        // TODO
      }
    ],
    "age": [
      {
        // TODO
      }
    ],
    
    // TODO
    
  }
}
```

## Project Example
- https://fnsapi.newslabfellows.com/fbnews

## Core Developers
- @todoaskit
- @Jiwoopark0508
