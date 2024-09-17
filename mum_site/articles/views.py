from django.db.models import Count
from django.shortcuts import render, redirect
from . models import Articles
from . forms import ArticlesForm
from django.views.generic import DetailView



def articles_home(request):
      articles = Articles.objects.order_by('-date')
      category = Articles.objects.values('category')
      return render(request, 'articles/index_article.html', {'articles': articles, "category": category})


def create(request):
     error = ''
     if request.method == 'POST':
         form = ArticlesForm(request.POST)
         if form.is_valid():
             form.save()
             return redirect('articles_home')
         else:
             error = 'Форма заполнена неверно'

     form = ArticlesForm()
     data = {'form': form, 'error': error}

     return render(request, 'articles/create_article.html', data)

class ArticleDetailView(DetailView):
     model = Articles
     context_object_name = 'article'
     template_name = 'articles/article_view.html'
