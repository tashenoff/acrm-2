
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls', namespace = 'main')),
    path('form/', include('main.urls', namespace = 'form')),
    path('home/', include('home.urls', namespace = 'home')),
    path('articles/', include('article.urls', namespace = 'article')), # нужен рефакторинг

    path('api/v1/home', include('home.urls'))
]

urlpatterns +=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
