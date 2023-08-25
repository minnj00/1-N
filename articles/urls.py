from django.urls import path
from . import views
app_name = 'articles'

urlpatterns=[
    path('', views.index, name='index'),
    path('<int:id>/detail/', views.detail, name='detail'),

    path('create/', views.create, name='create'),
    # -> 처음 create를 누르면 get 방식으로 진행됨.

    path('<int:article_id>/comments/create/', views.comment_create, name ='comment_create'),
    path('<int:article_id>/comments/<int:id>/delete', views.comment_delete, name = 'comment_delete'),

]