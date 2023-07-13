from django.db import models

from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from .utils import avatar_path


class AccountManager(BaseUserManager):
    def create_user(self, phone, password=None, **kwargs):
        if phone is None:
            raise TypeError({"success": False, "detail": _("User should have a phone")})
        user = self.model(phone=phone, **kwargs)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone, password=None, **kwargs):
        user = self.create_user(phone=phone, password=password, **kwargs)
        user.is_superuser = True
        user.is_staff = True
        user.is_active = True
        user.role = 0
        user.save(using=self._db)
        return user


class Account(AbstractBaseUser, PermissionsMixin):
    class Meta:
        verbose_name = 'Account'
        verbose_name_plural = 'Accounts'

    ROLE = (
        (0, 'Staff'),
        (1, 'Candidate'),
        (2, 'Recruiter'),
    )

    email = models.EmailField(max_length=12, unique=True, db_index=True)
    first_name = models.CharField(max_length=50, null=True)
    last_name = models.CharField(max_length=50, null=True)
    birth_date = models.DateField(null=True)
    avatar = models.ImageField(upload_to=avatar_path, null=True, blank=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    role = models.IntegerField(choices=ROLE, null=True)
    modified_date = models.DateTimeField(auto_now=True)
    created_date = models.DateTimeField(auto_now_add=True)

    objects = AccountManager()

    EMAIL_FIELD = ''
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    @property
    def full_name(self):
        name_list = []
        if self.last_name:
            name_list.append(self.last_name)
        if self.first_name:
            name_list.append(self.first_name)
        if name_list:
            return " ".join(name_list)
        return "-"


