from django.urls import path
# from news.api.views import article_detail_api_view, article_list_create_api_view
from news.api.views import ArticleListCreateApiView, ArticleDetailApiView

urlpatterns = [
    path("articles/", ArticleListCreateApiView.as_view(), name='article-list'),
    path("articles/<int:pk>/", ArticleDetailApiView.as_view(), name='article-detail')
]
