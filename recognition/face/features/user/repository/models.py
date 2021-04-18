from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

__all__ = ['CustomUser']


class UserManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError('Users must have an email address.')

        user = self.model(email=self.normalize_email(email))
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password):
        user = self.create_user(email, password=password)
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True

        user.save(using=self._db)

        return user


class CustomUser(AbstractUser):
    username = None
    address = models.CharField(max_length=30, blank=True, null=True, verbose_name='address')
    birthday = models.DateField(default=None, blank=True, null=True, verbose_name='birthday')
    email = models.EmailField(_('email'), unique=True)
    phone_number = models.CharField(max_length=13, blank=True, null=True, verbose_name='phone_number')
    student_id = models.CharField(max_length=13, blank=True, null=True, verbose_name='student_card')
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    class Meta:
        ordering = ['id']

    def __str__(self):
        return f'{self.email}'
