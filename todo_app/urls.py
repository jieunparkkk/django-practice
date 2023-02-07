from django.urls import path
from . import views

urlpatterns = [
    path('', views.Todos),
    # 클래스를 불러오기위해 .as_view()함수를 붙임
    path('create_todo/', views.TodoCreate.as_view()),

]