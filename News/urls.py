from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name = 'home'),
    path('category/<int:category_id>', category, name = 'category'),
    path('news/<int:news_id>', show_new, name='news'),
    path('news/add_news/', add_news, name='add_news'),
]