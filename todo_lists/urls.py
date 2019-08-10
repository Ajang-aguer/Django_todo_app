from django.urls import path

from todo_lists import views

app_name = 'todo_lists'
urlpatterns = [
    path('', views.home, name='home'),
    path('todolist/<int:todolist_id>/', views.todolist, name='todolist'),
    path('todolist/new/', views.new_todolist, name='new_todolist'),
    path('todolist/add/', views.add_todolist, name='add_todolist'),
    path('todo/add/<int:todolist_id>/', views.add_todo, name='add_todo'),
    path('todolists/', views.overview, name='overview'),
]