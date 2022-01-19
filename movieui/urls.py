from django.contrib import admin
from django.urls import path
from uiapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('detail/<str:movie_id>', views.detail, name='detail'),
]
