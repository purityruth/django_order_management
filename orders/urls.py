from django.urls import path
from django.contrib.auth.views import LogoutView
from social_django.views import AuthExceptionMiddleware, auth, complete

urlpatterns = [
    path('login/', auth, name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('complete/<backend>/', complete, name='complete'),
]
