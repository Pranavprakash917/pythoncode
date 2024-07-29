from django.urls import path
from . import views

urlpatterns = [
    path('insert/',views.insert,name='insert'),
    path('insert1/',views.insert1,name='insert1'),
    path('read/',views.read,name='read'),
    path('update/<int:id>/',views.update,name='update'),
    path('delete/<int:id>/',views.delete,name='delete'),
    path('create/',views.create_user,name='create_user'),
    path('login/',views.login,name='login'),
    path('email/',views.email,name='email')
]