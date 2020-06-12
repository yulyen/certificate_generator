from django.urls import path
from . import views

app_name = 'certgen'

urlpatterns = [
    path("", views.homepage, name='homepage'),
    path("register/", views.register, name='register'),
    path("logout/", views.logout_request, name='logout'),
    path("login/", views.login_request, name='login'),
    path("<single_slug>", views.single_slug, name='single_slug'),
    path("practice/", views.practice, name='practice'),
    path("api/orders/", views.orders, name='orders'), #for ajax practice
]
