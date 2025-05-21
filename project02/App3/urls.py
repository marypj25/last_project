from django.contrib import admin
from django.urls import path
from . import views

app_name = 'App3'
urlpatterns = [
    path('admin/', admin.site.urls),
    #path('', views.homepage, name='home_page'),
    path('home_page/<int:pk>', views.page, name='home_page'),
]





