from django.shortcuts import render, redirect
from .models import Article, Author, Comment
from .forms import ArticleForm, AuthorForm
from django.contrib.auth.decorators import login_required

def user_belongs_to_group(user, group):
    return user.groups.filter(name=group).exists()

def article_list(request):
    articles = Article.objects.all()
    canUserManipulate = request.user.groups.filter(name='Editores de artigos').exists()

    context = {'articles': articles,'canUserManipulate':canUserManipulate}
    return render(request, 'articles/article_list.html', context)

def article_detail(request, article_id):
    article = Article.objects.get(id=article_id)
    comments = Comment.objects.filter(article_id=article_id)
    canUserManipulate = request.user.groups.filter(name='Editores de artigos').exists()

    context = {'article': article, 'comments': comments, 'canUserManipulate':canUserManipulate}
    return render(request, 'articles/article_detail.html', context)


################################################################################
#
#                                   Artigo
#
################################################################################

@login_required
def create_article(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.fields['author'].initial = request.user
            article = form.save(commit=False)
            article.save()
            return redirect('articles:article_detail', article_id=article.id)
    else:
        form = ArticleForm()
    return render(request, 'articles/create_article.html', {'form': form})

@login_required
def edit_article(request, article_id):
    article = Article.objects.get(id=article_id)
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('articles:article_detail', article_id=article.id)
    else:
        form = ArticleForm(instance=article)
    return render(request, 'articles/edit_article.html', {'form': form, 'article': article})

@login_required
def delete_article(request, article_id):
    article = Article.objects.get(id=article_id)
    if request.method == 'POST':
        article.delete()
        return redirect('articles:article_list')

    return render(request, 'articles/delete_article.html', {'article': article})


################################################################################
#
#                                   Autor
#
################################################################################

@login_required
def create_author(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('articles:article_list')
    else:
        form = AuthorForm()
    return render(request, 'articles/create_author.html', {'form': form})

@login_required
def edit_author(request, author_id):
    author = Author.objects.get(id=author_id)
    if request.method == 'POST':
        form = AuthorForm(request.POST, instance=author)
        if form.is_valid():
            form.save()
            return redirect('articles:article_list')
    else:
        form = AuthorForm(instance=author)
    return render(request, 'articles/edit_author.html', {'form': form, 'author': author})

@login_required
def delete_author(request, author_id):
    author = Author.objects.get(id=author_id)
    if request.method == 'POST':
        author.delete()
        return redirect('articles:article_list')
    return render(request, 'articles/delete_author.html', {'author': author})











