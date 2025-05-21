from django.urls import path

from . import views

app_name = 'myApp2'
urlpatterns = [
    path('', views.index, name='index'),
    path('student_model_form/', views.student_model_form, name='student_model_form'),
    path('my_result/', views.my_result, name='my_result'),
    path('table/', views.table, name='table'),
    path('table_original/', views.table_original, name='table_original'),
]








