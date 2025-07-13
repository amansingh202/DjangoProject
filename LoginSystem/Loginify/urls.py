from django.urls import path
from . import views

urlpatterns = [
    path('', views.hello_world, name="hello"),
    path('signup/', views.signup, name = 'signup'),
    path('login/', views.login_view, name = 'login'),


    ## CRUD operations
    path('get-all-users/', views.get_all_users, name='get_all_users'),
    path('get-user/', views.get_user_by_email, name='get_user_by_email'),
    path('update-user/', views.update_user, name='update_user'),
    path('delete-user/', views.delete_user, name='delete_user'),
]