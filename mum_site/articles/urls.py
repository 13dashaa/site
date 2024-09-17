from django.urls import path
from . import views

urlpatterns = [
    path('', views.articles_home, name = 'articles_home'),
    path('create', views.create, name='create_article'),
    path('<int:pk>', views.ArticleDetailView.as_view(), name='articles_detail'),
#path('<int:pk>', views.ArticleDetailView.as_view(), name='articles_detail'),
]
