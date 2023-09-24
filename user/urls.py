from django.urls import path

from user.views import registration, login, profile, logout

app_name = 'user'

urlpatterns = [
    path('registration/', registration, name='registration'),
    path('login/', login, name='login'),
    path('profile/', profile, name='profile'),
    path('logout/', logout, name='logout'),
]
