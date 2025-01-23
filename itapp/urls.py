from django.urls import path
from .import views
from .views import sql_editor

urlpatterns = [
    path('', views.chatbot_view, name='chatbot'),
    path('2', views.sql_editor, name='sql_editor'),
    path("1", views.home, name='home'),
    path("<str:query>/", views.chat, name='chat'),
    path('send_message/', views.send_message, name='send_message'),
    path('view1/', views.view1, name='view1'),
    path('view2/', views.view2, name='view2'),
    path('view3/', views.view3, name='view3'),
    
]
