from .models import Author, User, Article, Comment, Rating
import json

Author.objects.all().delete()
Article.objects.all().delete()
Comment.objects.all().delete()
User.objects.all().delete()

with open('articles/json/authors.json') as f:
    authors = json.load(f)
    for author in authors:
        Author.objects.create(
            name=author['name'],
            photo=author['photo'],
        )


with open('articles/json/articles.json') as f:
    articles = json.load(f)
    for article in articles:
        Article.objects.create(
           title=article['title'],
           content=article['content'],
           author = Author.objects.get(name=article['author']),
        )

with open('articles/json/users.json') as f:
    users = json.load(f)
    for user in users:
        User.objects.create(
            name = user['name'],
        )

with open('articles/json/comments.json') as f:
    comments = json.load(f)
    for comment_info in comments:
        Comment.objects.create(
            comment = comment_info['comment'],
            author = User.objects.get(name = comment_info['author']),
            article = Article.objects.get(title = comment_info['article'])
        )

with open('articles/json/ratings.json') as f:
    ratings = json.load(f)
    for rating in ratings:
        Rating.objects.create(
            rating = rating['rating'],
            author = User.objects.get(name = rating['author']),
            article = Article.objects.get(title = rating['article'])
        )
