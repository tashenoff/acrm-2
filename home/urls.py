
from django.urls import path
from . import views


app_name = 'home'


urlpatterns = [
    path('', views.home, name='home'),
    path('/all/', views.RecordListView.as_view()),
    path('/record/create/', views.RecordCreateView.as_view()),
    path('/record/detail/<int:pk>/', views.RecordDetailView.as_view()),
]