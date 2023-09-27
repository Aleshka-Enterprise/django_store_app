from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView

from user.forms import UserLoginForm, UserRegistrationForm, UserProfileForm
from basket.models import Basket
from user.models import User


class UserRegistrationView(CreateView):
    model = User
    form_class = UserRegistrationForm
    template_name = 'user/registration.html'
    success_url = reverse_lazy('user:registration')


class UserLoginView(LoginView):
    template_name = 'user/login.html'
    form_class = UserLoginForm


class ProfileView(UpdateView):
    model = User
    template_name = 'user/profile.html'
    form_class = UserProfileForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['baskets'] = Basket.objects.filter(user=self.request.user)
        return context

    def get_success_url(self):
        return reverse_lazy('user:profile', kwargs={'pk': self.request.user.id})
