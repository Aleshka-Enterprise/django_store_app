from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LogoutView
from django.urls import path

from user.views import UserRegistrationView, UserLoginView, ProfileView, UserVerificationView

app_name = 'user'

urlpatterns = [
    path('registration/', UserRegistrationView.as_view(), name='registration'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('profile/<int:pk>', ProfileView.as_view(), name='profile'),
    path('logout/', login_required(LogoutView.as_view()), name='logout'),
    path('profile/verification/<uuid:id>', UserVerificationView.as_view(), name='user_verification')
]
