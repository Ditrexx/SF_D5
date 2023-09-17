from django.urls import path
from .views import NewsList, NewsDetailView, NewsSearchView, NewsCreateView, NewsUpdateView, NewsDeleteView, upgrade_me, IndexView

app_name = 'newapp'
urlpatterns = [
    path('', NewsList.as_view(), name='news'),
    path('news/<int:pk>', NewsDetailView.as_view(), name='news_detail'),
    path('search/', NewsSearchView.as_view(), name='news_search'),
    path('news/add/', NewsCreateView.as_view(), name='news_create'),
    path('news/<int:pk>/edit/', NewsUpdateView.as_view(), name='news_update'),
    path('news/<int:pk>/delete/', NewsDeleteView.as_view(), name='news_delete'),
    path('upgrade/', upgrade_me, name='upgrade'),
    path('index/', IndexView.as_view(), name='user_info')
]
