
from django.urls import path
from . import views
from .views import article, by_rubric, article_detail

app_name = 'article'


urlpatterns = [
    path('', article, name='index'),
    path('article/<int:article_id>/', article_detail, name='article_detail'),

    path('rubric/<int:rubric_id>/', by_rubric, name='by_rubric'),
]