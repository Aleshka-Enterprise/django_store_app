from django.db import models
from django.contrib.auth.models import AbstractUser
from products.models import Product


class User(AbstractUser):
    img = models.ImageField(upload_to='user_avatars')
