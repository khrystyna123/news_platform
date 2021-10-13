# News Platform

It's a simple API that have a list of news with functionality to upvote and comment on them.

## Setup 

Run following commands to set up and run project with Docker.

```
git clone <project.url> <project>
cd <project>
docker-compose up -d --build
docker-compose exec web python manage.py migrate --noinput
docker run news_platform_web
```

## Link to Postman Collection

https://www.getpostman.com/collections/9b6181c4db770965650f

## Deployment Link

https://news-platform-001.herokuapp.com/api/v1/news/