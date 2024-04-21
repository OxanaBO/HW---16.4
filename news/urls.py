from django.urls import path
# Импортируем созданное нами представление
from .views import (
    PostsList, PostDetail, ArticleCreate, ArticleUpdate, NewsCreate,
    NewsUpdate, PostSearch, ArticleDelete, NewsDelete, CategoryListView, subscribe
)


urlpatterns = [
    path('', PostsList.as_view(), name='post_list'),
    path('<int:pk>', PostDetail.as_view(), name='post_detail'),
    path('search/', PostSearch.as_view(), name='post_search'),
    path('articles/create/', ArticleCreate.as_view(), name='articles_create'),
    path('articles/<int:pk>/edit/', ArticleUpdate.as_view(), name='articles_edit'),
    path('news/create/', NewsCreate.as_view(), name='news_create'),
    path('news/<int:pk>/edit/', NewsUpdate.as_view(), name='news_edit'),
    path('articles/<int:pk>/delete/', ArticleDelete.as_view(), name='articles_delete'),
    path('news/<int:pk>/delete/', NewsDelete.as_view(), name='news_delete'),
    path('categories/<int:pk>', CategoryListView.as_view(), name='category_list'),
    path('categories/<int:pk>/subscribe', subscribe, name='subscribe'),
]
