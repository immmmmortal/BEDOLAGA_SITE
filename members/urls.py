from django.urls import path

from phonestore import views

urlpatterns = [
    path('user_registration', views.registration_page, name='user_registration'),
    path('user_login', views.login_page, name='user_login'),
    path('user_logout', views.logout_user, name='user_logout'),

]
