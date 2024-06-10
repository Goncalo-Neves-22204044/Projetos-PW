from django.contrib import admin
from .models import Author
from .models import User
from .models import Article
from .models import Comment
from .models import Rating

# Register your models here.

admin.site.register(Author)
admin.site.register(User)
admin.site.register(Article)
admin.site.register(Comment)
admin.site.register(Rating)