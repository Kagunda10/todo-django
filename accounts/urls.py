from django.urls import path

from . import views


urlpatterns = [
    path('signup/', views.signup_view, name='signup'),
    path('password_reset/', views.password_reset_view, name='password_reset'),
    path('reset/', views.password_set_view, name='reset')
]