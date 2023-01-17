from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='home'), #http://127.0.0.1:7000
    path('juds/', judging, name='juds'),
    path('table/', table, name='table'),
    path('entrance/', LoginUser.as_view(), name='input'),
    path('logout/', LogoutUser, name='logout'),
    path('category/<int:cat_id>/', show_category, name='category'),
    path('update/<int:pk>/', NewsUpdateView.as_view(), name='update'),
]