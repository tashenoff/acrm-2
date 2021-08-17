
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls', namespace = 'main')),
    path('home/', include('home.urls', namespace = 'home')),
    path('api/v1/home', include('home.urls'))
]
