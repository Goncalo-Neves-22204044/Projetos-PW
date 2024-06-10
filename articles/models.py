from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Author(models.Model):
    name = models.CharField(max_length = 100)
    photo = models.ImageField(null=True)

    def __str__(self):
        return f'{self.name}'

class User(models.Model):
    name = models.CharField(max_length = 100)

    def __str__(self):
        return f'{self.name}'

class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name = 'articles')
    release_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.title}'

class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    comment = models.TextField()
    release_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.author.name} in {self.article.title}"

class Rating(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='ratings')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='ratings')
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)])

    def __str__(self):
        return f"{self.rating}/10 to {self.article.title} by {self.author.name}"
