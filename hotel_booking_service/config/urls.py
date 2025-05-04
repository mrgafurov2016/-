from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('hotels.urls')),  # подключаем urls.py из приложения hotels
]


