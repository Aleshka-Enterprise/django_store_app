from django.conf import settings
from django.core.mail import send_mail
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse

from products.models import Product


class User(AbstractUser):
    img = models.ImageField(upload_to='user_avatars')
    email_is_verified = models.BooleanField(default=False, verbose_name='Почта подтверждена')


class EmailVerification(models.Model):
    uuid = models.UUIDField(unique=True)
    date_of_creation = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)
    date_of_expiration = models.DateTimeField(verbose_name='Срок окончания действия кода')
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)

    def __str__(self):
        return f'Подтвердить почту {self.user.email}'

    def send_verification_mail(self):
        link = reverse('user:user_verification', kwargs={'id': self.uuid})
        message = f'''Для подтверждения учётной записи для {self.user.username} перейдите по ссылке:
        {settings.DOMAIN_NAME}{link}
        '''
        send_mail(
            subject=f'Подтверждение учётной записи для {self.user.username}',
            message=message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[self.user.email],
            fail_silently=False
        )
