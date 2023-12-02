from django.urls import path
from .views import *

urlpatterns = [
    path('home/', home_view, name='home_view'),
    path('users/', users_view, name='users_view'),
    path('manders/', manders_view, name='manders_view'),
    path('edit_user/<int:user_id>/', edit_user_view, name='edit_user'),
    

]