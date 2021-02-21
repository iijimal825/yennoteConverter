from django.urls import path
from . import views

app_name='app'

urlpatterns = [
#    path('login/', views.Login.as_view(), name='login'),
#    path('logout/', views.Logout.as_view(), name='logout'), 
    path('', views.index, name='index'),
    path('detail/<int:pk>/', views.detail, name='detail'),
    path('analyze/<int:pk>/', views.analyze, name='analyze'),
    path('new_file/', views.new_file, name='new_file'), 
]